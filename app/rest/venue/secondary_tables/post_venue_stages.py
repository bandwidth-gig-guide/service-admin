from app.query.execute import execute
from app.model.venue_stage_insert import VenueStageInsert
from uuid import UUID
from typing import List

def post_venue_stages(stages: List[VenueStageInsert], venue_id: UUID, connection, cursor):
    if stages:
        for stage in stages:
            execute(
            """
                INSERT INTO VenueStage (VenueID, Title, Description, Capacity)
                VALUES (%s, %s, %s, %s)
            """,
                (venue_id, stage.Title, stage.Description, stage.Capacity),
                connection=connection,
                cursor=cursor
            )