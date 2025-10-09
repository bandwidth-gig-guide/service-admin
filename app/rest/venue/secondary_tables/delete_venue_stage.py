from app.query.execute_with_return import execute as execute_with_return
from app.query.execute import execute
from uuid import UUID
from typing import List, Optional

def delete_venue_stage(stages_to_keep: Optional[List[UUID]], venue_id: UUID, connection, cursor):
    
    if not stages_to_keep:
        raise ValueError("Venue must have at least one stage")


    events_using_stage: List[tuple] = execute_with_return(check_one(), check_one_values(stages_to_keep), connection, cursor)
    if events_using_stage:
        raise ValueError(
            "Cannot delete stages allocated to events: "
            + ", ".join(str(event[0]) for event in events_using_stage)
        )

    venue_has_another_stage: bool = execute_with_return(check_two(), check_two_values(stages_to_keep), connection, cursor)[0][0]
    if not venue_has_another_stage:
        raise ValueError("Venue must have at least one stage")
    
    execute(delete(), delete_values(venue_id, stages_to_keep), connection, cursor)



def check_one():
    return """
        SELECT EventID, Title, StageID
        FROM Event
        WHERE StageID = ANY(%s)
    """

def check_one_values(stages_to_keep: List[UUID]):
    return (tuple(str(stage) for stage in stages_to_keep),)



def check_two():
    return """
        SELECT EXISTS (
            SELECT 1 FROM VenueStage
            WHERE VenueID = %s
            AND VenueStageID != ALL(%s)
        )
    """

def check_two_values(venue_id: UUID, stages_to_keep: List[UUID]):
    return (
        str(venue_id),
        tuple(str(stage) for stage in stages_to_keep)
    )



def delete():
    return """
        DELETE FROM VenueStage
        WHERE VenueID = %s
        AND VenueStageID != ALL(%s)
    """

def delete_values(venue_id: UUID, stages_to_keep: List[UUID]):
    return (
        str(venue_id),
        tuple(str(stage) for stage in stages_to_keep)
    )
