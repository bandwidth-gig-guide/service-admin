from app.query.execute import execute
from uuid import UUID
from typing import Optional, List

def post_event_social(socials: Optional[List[str]], event_id: UUID, connection, cursor):
    if socials:
        for social in socials:
            execute(
            """
                INSERT INTO EventSocial (EventID, SocialPlatform, Handle, Url)
                VALUES (%s, %s, %s, %s)
            """,
                (str(event_id), social.SocialPlatform, social.Handle, str(social.Url)),
                connection=connection,
                cursor=cursor
            )