from app.query.execute import execute
from app.model.event_performance_insert import EventPerformanceInsert
from app.rest.event.secondary_tables.post_event_performance import post_event_performance
from uuid import UUID
from typing import List

def put_event_performance(performances: List[EventPerformanceInsert], event_id: UUID, connection, cursor):
    execute(delete_existing_performances(), (str(event_id),), connection, cursor)
    post_event_performance(performances, event_id, connection, cursor)
                

def delete_existing_performances(): 
    return """
        DELETE FROM EventPerformance
        WHERE EventID = %s;
    """
    