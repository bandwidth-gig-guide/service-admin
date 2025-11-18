from app.query.execute import execute
from app.model.venue_stage_insert import VenueStageInsert
from uuid import UUID
from typing import Optional, List
from app.rest.venue.secondary_tables.post_venue_stage import post_venue_stage
from app.rest.venue.secondary_tables.delete_venue_stage import delete_venue_stage

def put_venue_stage(stages: Optional[List[VenueStageInsert]], venue_id: UUID, connection, cursor):

    stage_ids = [stage.StageID for stage in stages if stage.StageID]
    delete_venue_stage(stage_ids, venue_id, connection, cursor)

    if stages:
        updated_stages: List[VenueStageInsert] = [stage for stage in stages if stage.StageID]
        new_stages: List[VenueStageInsert] = [stage for stage in stages if not stage.StageID]

        if updated_stages:
            for stage in updated_stages:
                execute(update_updated_stage(), value_updated_stage(stage), connection, cursor)

        if new_stages:
            post_venue_stage(new_stages, venue_id, connection, cursor)

    

def update_updated_stage():
    return """
        UPDATE VenueStage
        SET Title = %s, Description = %s, Capacity = %s
        WHERE StageID = %s
    """

def value_updated_stage(stage: VenueStageInsert):
    return (
        stage.Title,
        stage.Description,
        stage.Capacity,
        str(stage.StageID)
    )
