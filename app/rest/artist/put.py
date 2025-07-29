from app.query.execute_with_return import execute as execute_with_return
from app.query.execute import execute
from app.db.connection import get_db_connection
from app.model.artist_insert import ArtistInsert
from uuid import UUID
from typing import Optional, List
from pydantic import HttpUrl
from psycopg2 import DatabaseError


def put(artist_id: UUID, artist: ArtistInsert):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                update_artist(artist_id, artist, connection, cursor)
                delete_related_artist_data(artist_id, connection, cursor)
                post_artist_type(artist.Types, artist_id, connection, cursor)
                post_artist_tag(artist.Tags, artist_id, connection, cursor)
                post_artist_social(artist.Socials, artist_id, connection, cursor)
                post_artist_image(artist.ImageUrls, artist_id, connection, cursor)
                connection.commit()
                return artist_id
            except DatabaseError:
                connection.rollback()
                raise


# Update Artist Table
def update_artist(artist_id: UUID, artist: ArtistInsert, connection, cursor):
    execute(
    """
        UPDATE Artist SET
            Title = %s,
            Country = %s,
            City = %s,
            StateCode = %s,
            YearFounded = %s,
            Description = %s,
            SpotifyEmbedURL = %s,
            YoutubeEmbedURL = %s
        WHERE ArtistID = %s
    """,
        (
            artist.Title,
            artist.Country,
            artist.City,
            artist.StateCode,
            artist.YearFounded,
            artist.Description,
            str(artist.SpotifyEmbedURL) if artist.SpotifyEmbedURL else None,
            str(artist.YoutubeEmbedURL) if artist.YoutubeEmbedURL else None,
            str(artist_id)
        ),
        connection=connection,
        cursor=cursor
    )


# Delete previous related records
def delete_related_artist_data(artist_id: UUID, connection, cursor):
    execute("DELETE FROM ArtistType WHERE ArtistID = %s", (str(artist_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM ArtistTag WHERE ArtistID = %s", (str(artist_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM ArtistSocial WHERE ArtistID = %s", (str(artist_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM ArtistImage WHERE ArtistID = %s", (str(artist_id),), connection=connection, cursor=cursor)


# ArtistType Table
def post_artist_type(types: Optional[List[str]], artist_id: UUID, connection, cursor):
    if types:
        for type_ in types:
            execute(
            """
                INSERT INTO ArtistType (ArtistID, Type) 
                VALUES (%s, %s)
            """,
                (str(artist_id), type_),
                connection=connection,
                cursor=cursor
            )


# ArtistTag Table
def post_artist_tag(tags: Optional[List[str]], artist_id: UUID, connection, cursor):
    if tags:
        for tag in tags:
            execute(
            """
                INSERT INTO ArtistTag (ArtistID, Tag)
                VALUES (%s, %s)
            """,
                (str(artist_id), tag),
                connection=connection,
                cursor=cursor
            )


# ArtistSocial Table
def post_artist_social(socials: Optional[List[str]], artist_id: UUID, connection, cursor):
    if socials:
        for social in socials:
            execute(
            """
                INSERT INTO ArtistSocial (ArtistID, SocialPlatform, Handle, Url)
                VALUES (%s, %s, %s, %s)
            """,
                (str(artist_id), social.SocialPlatform, social.Handle, str(social.Url)),
                connection=connection,
                cursor=cursor
            )


# ArtistImage / Image Tables
def post_artist_image(imageUrls: Optional[list[HttpUrl]], artist_id: UUID, connection, cursor):
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
                INSERT INTO ArtistImage (ArtistID, ImageID, DisplayOrder)
                VALUES (%s, %s, %s)
            """,
                (str(artist_id), str(image_id), index + 1),
                connection=connection,
                cursor=cursor
            )