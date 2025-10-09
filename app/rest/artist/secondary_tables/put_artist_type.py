from app.query.execute import execute
from app.rest.artist.secondary_tables.post_artist_type import post_artist_type
from uuid import UUID
from typing import Optional, List

def put_artist_type(types: Optional[List[str]], artist_id: UUID, connection, cursor):
    execute(delete_existing_types(), str(artist_id), connection, cursor)
    post_artist_type(types, artist_id, connection, cursor)
                

def delete_existing_types(): 
    return """
        DELETE FROM ArtistType
        WHERE ArtistID = %s;
    """
    