from app.query.execute_with_return_multiple_rows import execute as execute_with_return
from app.query.execute import execute
from uuid import UUID
from typing import List, Optional

def delete_venue_stage(stages_to_keep: Optional[List[UUID]], venue_id: UUID, connection, cursor):
    
    if not stages_to_keep:
        raise ValueError("Venue must have at least one stage")
    
    stages_to_delete: List[tuple] = execute_with_return(get_stages_to_delete(), get_stages_to_delete_values(venue_id, stages_to_keep), connection, cursor)
    if not stages_to_delete:
        return

    events_using_stage: List[tuple] = execute_with_return(check_one(), check_one_values(stages_to_delete), connection, cursor)
    if events_using_stage:
        raise ValueError(
            "Cannot delete stages "
            + ", ".join(str(stage[0]) for stage in stages_to_delete)
            + " allocated to events: "
            + ", ".join(str(event[0]) for event in events_using_stage)
        )

    venue_has_another_stage: bool = execute_with_return(check_two(), check_two_values(venue_id, stages_to_delete), connection, cursor)[0][0]
    if not venue_has_another_stage:
        raise ValueError("Venue must have at least one stage")
    
    execute(delete(), delete_values(venue_id, stages_to_delete), connection, cursor)


def get_stages_to_delete():
    return """
        SELECT StageID
        FROM VenueStage
        WHERE VenueID = %s
        AND StageID != ALL(%s::uuid[])
    """

def get_stages_to_delete_values(venue_id: UUID, stages_to_keep: List[UUID]):
    return (
        str(venue_id),
        [str(stage) for stage in stages_to_keep]
    )


def check_one():
    return """
        SELECT EventID, Title, StageID
        FROM Event
        WHERE StageID = ANY(%s::uuid[])
    """

def check_one_values(stages_to_keep: List[UUID]):
    return ([str(stage[0]) for stage in stages_to_keep],)



def check_two():
    return """
        SELECT EXISTS (
            SELECT 1 FROM VenueStage
            WHERE VenueID = %s
            AND StageID != ALL(%s::uuid[])
        )
    """

def check_two_values(venue_id: UUID, stages_to_keep: List[UUID]):
    return (
        str(venue_id),
        list(str(stage) for stage in stages_to_keep)
    )



def delete():
    return """
        DELETE FROM VenueStage
        WHERE VenueID = %s
        AND VenueStageID != ALL(%s::uuid[])
    """

def delete_values(venue_id: UUID, stages_to_keep: List[UUID]):
    return (
        str(venue_id),
        list(str(stage) for stage in stages_to_keep)
    )