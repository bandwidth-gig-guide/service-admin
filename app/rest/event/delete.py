from app.query.execute import execute
from uuid import UUID

def delete(event_id: UUID):
    execute(query(), values(event_id))

def query():
    return "DELETE FROM Event WHERE EventID = %s"

def values(event_id: UUID):
    return (str(event_id),)