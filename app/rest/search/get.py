from typing import List, Optional
from app.query.fetch_list import execute

def get(record_types: Optional[List[str]] = None, search_string: Optional[str] = None, limit: Optional[int] = None) -> dict:
    result = {}
        
    if not record_types:
        record_types = ["event", "artist", "venue"]

    for record_type in record_types:
        if record_type.lower() in ["event", "artist", "venue"]:
            sql, values = query(record_type, search_string, limit)
            response = execute(sql, values)
            result[f"{record_type.lower()}"] = [{"id": row[0], "title": row[1]} for row in response]

    return result

def query(record_type: str, search_string: Optional[str] = None, limit: Optional[int] = None):
    table_map = {
        "event": "Event",
        "artist": "Artist",
        "venue": "Venue"
    }

    table_name = table_map[record_type.lower()]
    id_column = f"{table_name}ID"

    sql = f"""
        SELECT
            {id_column},
            Title
        FROM {table_name}
    """

    values = []

    if search_string:
        sql += """
            WHERE LOWER(Title) LIKE %s
               OR CAST({id_column} AS TEXT) LIKE %s
        """.format(id_column=id_column)

        like_value = f"%{search_string.lower()}%"
        values.extend([like_value, like_value])

    sql += " ORDER BY Title"

    if limit:
        sql += " LIMIT %s"
        values.append(limit)

    return sql, tuple(values)
