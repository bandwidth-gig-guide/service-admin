from app.query.execute import execute
from app.rest.artist.secondary_tables.post_artist_social import post_artist_social
from uuid import UUID
from typing import Optional, List

def put_artist_social(socials: Optional[List[str]], artist_id: UUID, connection, cursor):
    execute(delete_existing_socials(), str(artist_id), connection, cursor)
    post_artist_social(socials, artist_id, connection, cursor)
                

def delete_existing_socials(): 
    return """
        DELETE FROM ArtistSocial 
        WHERE ArtistID = %s
    """
    