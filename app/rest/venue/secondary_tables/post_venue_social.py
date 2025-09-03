from app.query.execute import execute
from uuid import UUID
from typing import Optional, List

def post_venue_social(socials: Optional[List[str]], venue_id: UUID, connection, cursor):
    if socials:
        for social in socials:
            execute(
            """
                INSERT INTO VenueSocial (VenueID, SocialPlatform, Handle, Url)
                VALUES (%s, %s, %s, %s)
            """,
                (str(venue_id), social.SocialPlatform, social.Handle, str(social.Url)),
                connection=connection,
                cursor=cursor
            )