from app.query.execute import execute
from uuid import UUID
from typing import Optional, List

def post_artist_social(socials: Optional[List[str]], artist_id: UUID, connection, cursor):
    if socials:
        for social in socials:
            execute(
            """
                INSERT INTO ArtistSocial (ArtistID, SocialPlatform, Handle, Url)
                VALUES (%s, %s, %s, %s)
            """,
                (str(artist_id), social.SocialPlatform, social.Handle, str(social.Url)),
                connection=connection,
                cursor=cursor
            )