from app.query.execute import execute
from app.rest.venue.secondary_tables.post_venue_social import post_venue_social
from uuid import UUID
from typing import Optional, List

def put_venue_social(socials: Optional[List[str]], venue_id: UUID, connection, cursor):
    execute(delete_existing_socials(), (str(venue_id),), connection, cursor)
    post_venue_social(socials, venue_id, connection, cursor)
                

def delete_existing_socials(): 
    return """
        DELETE FROM VenueSocial 
        WHERE VenueID = %s
    """
    