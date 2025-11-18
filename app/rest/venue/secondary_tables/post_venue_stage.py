from app.query.execute import execute
from app.model.venue_stage_insert import VenueStageInsert
from uuid import UUID
from typing import List

def post_venue_stage(stages: List[VenueStageInsert], venue_id: UUID, connection, cursor):
    if stages:
        for stage in stages:
            execute(
            """
                INSERT INTO VenueStage (Title, Description, Capacity)
                VALUES (%s, %s, %s)
            """,
                (stage.Title, stage.Description, stage.Capacity),
                connection=connection,
                cursor=cursor
            )