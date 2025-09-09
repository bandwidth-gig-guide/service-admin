from typing import List
from app.query.fetch_list import execute

def get_all_id_and_title() -> List[dict]:
    response = execute(query())
    return [{"VenueID": row[0], "Title": row[1], "StageID": row[2], "StageTitle": row[3]} for row in response]

def query():
    return """
        SELECT
            Venue.VenueID,
            Venue.Title,
            VenueStage.StageID,
            VenueStage.Title
        FROM Venue
        JOIN VenueStage ON VenueStage.VenueID = Venue.VenueID
        ORDER BY 
            Venue.Title, 
            VenueStage.Title
    """