from app.query.execute import execute
from uuid import UUID

def delete(venue_id: UUID):
    execute(query(), values(venue_id))

def query():
    return "DELETE FROM Venue WHERE VenueID = %s"

def values(venue_id: UUID):
    return (str(venue_id),)