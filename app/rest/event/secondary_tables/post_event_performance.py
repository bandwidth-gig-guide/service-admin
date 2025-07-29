from app.query.execute import execute
from app.model.event_performance_insert import EventPerformanceInsert
from uuid import UUID
from typing import List

def post_event_performance(performances: List[EventPerformanceInsert], event_id: UUID, connection, cursor):
    if performances:
        for performance in performances:
            execute(
            """
                INSERT INTO EventPerformance (
                    EventID, 
                    ArtistID, 
                    SetListPosition,
                    StartDateTime,
                    EndDateTime
                )
                VALUES (%s, %s, %s, %s, %s)
            """,
                (
                    str(event_id), 
                    str(performance.ArtistID),
                    performance.SetListPosition,
                    performance.StartDateTime,
                    performance.EndDateTime
                ),
                connection=connection,
                cursor=cursor
            )