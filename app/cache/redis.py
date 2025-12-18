import os
import json
import hashlib
from typing import Callable, Any
import redis
from pydantic import BaseModel
from app.cache.key import KEYS_INDIVIDUAL, KEYS_UNIVERSAL, KEYS_UNIVERSAL_FILTERABLE


REDIS_HOST = os.getenv("REDIS_HOST", "")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
CACHE_DISABLED = REDIS_HOST == ""

DEFAULT_TTL: int = 300

_redis = None

def _init_redis():
    global _redis
    if CACHE_DISABLED:
        return

    try:
        _redis = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True,
            socket_connect_timeout=1,
            socket_timeout=1,
        )
        _redis.ping()
    except Exception:
        _redis = None
        print("Redis Unavailable. Cache Disabled")

_init_redis()


def _hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()


def make_key(base: str, record_id: str = None, **params) -> str:
    parts = [base]

    if record_id is not None:
        parts.append(str(record_id))

    if params:
        normalized = "|".join(
            f"{key}={sorted(value) if isinstance(value, list) else value}"
            for key, value in sorted(params.items())
            if value is not None
        )
        parts.append(_hash(normalized))

    return ":".join(parts)


def cache_wrap(key: str, fetch_fn: Callable[[], Any], ttl: int = DEFAULT_TTL, ):
    if CACHE_DISABLED or _redis is None:
        return fetch_fn()

    try:
        cached = _redis.get(key)
        if cached is not None:
            return json.loads(cached)

        data = fetch_fn()

        if isinstance(data, BaseModel):
            data_to_cache = data.dict()
        elif isinstance(data, list) and data and isinstance(data[0], BaseModel):
            data_to_cache = [item.dict() for item in data]
        else:
            data_to_cache = data

        _redis.setex(key, ttl, json.dumps(data_to_cache, default=str))
        return data_to_cache

    except Exception as e:
        print(f"[CACHE] Redis error: {e}")
        return fetch_fn()


def invalidate_cache(record_type: str, record_id: str = None, **params):
    if _redis is None:
        return

    try:
        pipe = _redis.pipeline()

        if record_id:
            for key_base in KEYS_INDIVIDUAL.get(record_type, []):
                cache_key = make_key(key_base, record_id=record_id)
                pipe.delete(cache_key)

        for key_base in KEYS_UNIVERSAL.get(record_type, []):
            cache_key = make_key(key_base)
            pipe.delete(cache_key)

        for key_base in KEYS_UNIVERSAL_FILTERABLE.get(record_type, []):
            if params:
                cache_key = make_key(key_base, **params)
                pipe.delete(cache_key)
            else:
                for key_with_params in _redis.scan_iter(f"{key_base}:*"):
                    pipe.delete(key_with_params)

        pipe.execute()

    except Exception as e:
        print(f"[CACHE] Failed to invalidate cache for record_type={record_type}, record_id={record_id}: {e}")
