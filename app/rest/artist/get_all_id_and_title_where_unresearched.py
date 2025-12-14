from typing import List
from app.query.fetch_list import execute

def get_all_id_and_title() -> List[dict]:
    response = execute(query())
    return [{
        "ArtistID": row[0], 
        "Title": row[1],
        "UpcomingEventCount": row[2],
        "NextEventDateTime": row[3]
    } for row in response]

def query():
    return """
        SELECT
            Artist.ArtistID,
            Artist.Title,
            COUNT(EventPerformance) AS UpcomingEventCount,
            MIN(EventPerformance.StartDateTime) AS NextEventDateTime
        FROM Artist
        JOIN EventPerformance ON EventPerformance.ArtistID = Artist.ArtistID
        WHERE Artist.IsResearched IS FALSE
        GROUP BY Artist.ArtistID, Artist.Title, EventPerformance.StartDateTime
        ORDER BY 
            EventPerformance.StartDateTime ASC, 
            UpcomingEventCount DESC, 
            Artist.Title ASC
    """