from app.query.execute import execute
from app.model.opening_hours import OpeningHours
from uuid import UUID
from typing import Optional

def put_venue_opening_hours(hours: Optional[OpeningHours], venue_id: UUID, connection, cursor):
    if hours:
        execute(query(), value(hours, venue_id), connection, cursor)


def query():
    return """
        UPDATE VenueOpeningHours
        SET
            MonOpen = %s, MonClose = %s,
            TueOpen = %s, TueClose = %s,
            WedOpen = %s, WedClose = %s,
            ThurOpen = %s, ThurClose = %s,
            FriOpen = %s, FriClose = %s,
            SatOpen = %s, SatClose = %s,
            SunOpen = %s, SunClose = %s
        WHERE VenueID = %s;
    """

def value(hours: OpeningHours, venue_id: UUID):
    return (
        hours.MonOpen, hours.MonClose,
        hours.TueOpen, hours.TueClose,
        hours.WedOpen, hours.WedClose,
        hours.ThurOpen, hours.ThurClose,
        hours.FriOpen, hours.FriClose,
        hours.SatOpen, hours.SatClose,
        hours.SunOpen, hours.SunClose,
        str(venue_id)
    )