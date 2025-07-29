from app.query.execute_with_return import execute as execute_with_return
from app.query.execute import execute
from app.db.connection import get_db_connection
from app.model.venue_insert import VenueInsert
from app.model.venue_stage_insert import VenueStageInsert
from app.model.opening_hours import OpeningHours
from uuid import UUID
from typing import Optional, List
from pydantic import  HttpUrl
from psycopg2 import DatabaseError


def post(venue: VenueInsert) -> UUID:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                venue_id: UUID = post_venue(venue, connection, cursor)
                post_venue_type(venue.Types, venue_id, connection, cursor)
                post_venue_tag(venue.Tags, venue_id, connection, cursor)
                post_venue_social(venue.Socials, venue_id, connection, cursor)
                post_venue_image(venue.ImageUrls, venue_id, connection, cursor)
                post_venue_stages(venue.VenueStages, venue_id, connection, cursor)
                post_opening_hours(venue.OpeningHours, venue_id, connection, cursor)
                connection.commit()
                return venue_id
            except DatabaseError:
                connection.rollback()
                raise


# Venue Table
def post_venue(venue: VenueInsert, connection, cursor) -> UUID:
    response = execute_with_return(
    """
        INSERT INTO Venue (
            Title,
            StreetAddress,
            City,
            StateCode,
            PostCode,
            Description,
            WebsiteURL,
            PhoneNumber,
            GoogleMapsEmbedURL
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING VenueID
    """,
        venue.Title,
        venue.StreetAddress,
        venue.City,
        venue.StateCode,
        venue.PostCode,
        venue.Description,
        str(venue.WebsiteUrl) if venue.WebsiteUrl else None,
        venue.PhoneNumber,
        str(venue.GoogleMapsEmbedUrl),
        connection=connection,
        cursor=cursor
    )
    return response[0]


# VenueType Table
def post_venue_type(types: Optional[List[str]], venue_id: UUID, connection, cursor):
    if types:
        for type_ in types:
            execute(
            """
                INSERT INTO VenueType (VenueID, Type) 
                VALUES (%s, %s)
            """,
                (venue_id, type_),
                connection=connection,
                cursor=cursor
            )


# VenueTag Table
def post_venue_tag(tags: Optional[List[str]], venue_id: UUID, connection, cursor):
    if tags:
        for tag in tags:
            execute(
            """
                INSERT INTO VenueTag (VenueID, Tag)
                VALUES (%s, %s)
            """,
                (venue_id, tag),
                connection=connection,
                cursor=cursor
            )


# VenueSocial Table
def post_venue_social(socials: Optional[List[str]], venue_id: UUID, connection, cursor):
    if socials:
        for social in socials:
            execute(
            """
                INSERT INTO VenueSocial (VenueID, SocialPlatform, Handle, Url)
                VALUES (%s, %s, %s, %s)
            """,
                (venue_id, social.SocialPlatform, social.Handle, str(social.Url)),
                connection=connection,
                cursor=cursor
            )


# VenueImage / Image Tables
def post_venue_image(imageUrls: Optional[list[HttpUrl]], venue_id: UUID, connection, cursor):
    if imageUrls:
        for index, url in enumerate(imageUrls):
            response = execute_with_return(
            """
                INSERT INTO Image (Url) 
                VALUES (%s)
                RETURNING ImageID
            """,
                (str(url)),
                connection=connection,
                cursor=cursor
            )
            image_id: UUID = response[0]

            execute(
            """
                INSERT INTO VenueImage (VenueID, ImageID, DisplayOrder)
                VALUES (%s, %s, %s)
            """,
                (venue_id, image_id, index + 1),
                connection=connection,
                cursor=cursor
            )

# VenueStage
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


# VenueOpeningHours
def post_opening_hours(hours: Optional[OpeningHours], venue_id: UUID, connection, cursor):
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