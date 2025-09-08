from typing import List
from app.query.fetch_list import execute

def get_all_id_and_title() -> List[dict]:
    response = execute(query())
    return [{"ArtistID": row[0], "Title": row[1]} for row in response]

def query():
    return """
        SELECT
            ArtistID,
            Title 
        FROM Artist
        ORDER BY Title
    """
