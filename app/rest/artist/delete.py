from app.query.execute import execute
from uuid import UUID

def delete(artist_id: UUID):
    execute(query(), values(artist_id))

def query():
    return "DELETE FROM Artist WHERE ArtistID = %s"

def values(artist_id: UUID):
    return (str(artist_id),)