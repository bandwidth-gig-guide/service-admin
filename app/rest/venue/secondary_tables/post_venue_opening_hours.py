from app.query.execute import execute
from app.model.opening_hours import OpeningHours
from uuid import UUID
from typing import Optional

def post_venue_opening_hours(hours: Optional[OpeningHours], venue_id: UUID, connection, cursor):
    if hours:
        execute(
        """
            INSERT INTO VenueOpeningHours (
                VenueID,
                MonOpen, MonClose,
                TueOpen, TueClose,
                WedOpen, WedClose,
                ThurOpen, ThurClose,
                FriOpen, FriClose,
                SatOpen, SatClose,
                SunOpen, SunClose
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
            (
                venue_id,
                hours.MonOpen, hours.MonClose,
                hours.TueOpen, hours.TueClose,
                hours.WedOpen, hours.WedClose,
                hours.ThurOpen, hours.ThurClose,
                hours.FriOpen, hours.FriClose,
                hours.SatOpen, hours.SatClose,
                hours.SunOpen, hours.SunClose
            ),
            connection=connection,
            cursor=cursor
        )