from app.query.execute import execute
from app.rest.artist.secondary_tables.post_artist_tag import post_artist_tag
from uuid import UUID
from typing import Optional, List

def put_artist_tag(tags: Optional[List[str]], artist_id: UUID, connection, cursor):
    execute(delete_existing_tags(), str(artist_id), connection, cursor)
    post_artist_tag(tags, artist_id, connection, cursor)
                

def delete_existing_tags(): 
    return """
        DELETE FROM ArtistTag
        WHERE ArtistID = %s;
    """
    