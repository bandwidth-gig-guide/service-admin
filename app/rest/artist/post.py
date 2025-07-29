from app.query.execute_with_return import execute as execute_with_return
from app.query.execute import execute
from app.db.connection import get_db_connection
from app.model.artist_insert import ArtistInsert
from uuid import UUID
from typing import Optional, List
from pydantic import  HttpUrl
from psycopg2 import DatabaseError


def post(artist: ArtistInsert) -> UUID:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                artist_id: UUID = post_artist(artist, connection, cursor)
                post_artist_type(artist.Types, artist_id, connection, cursor)
                post_artist_tag(artist.Tags, artist_id, connection, cursor)
                post_artist_social(artist.Socials, artist_id, connection, cursor)
                post_artist_image(artist.ImageUrls, artist_id, connection, cursor)
                connection.commit()
                return artist_id
            except DatabaseError:
                connection.rollback()
                raise


# Artist Table
def post_artist(artist: ArtistInsert, connection, cursor) -> UUID:
    response = execute_with_return(
    """
        INSERT INTO Artist (
            Title,
            Country,
            City,
            StateCode,
            YearFounded,
            Description,
            SpotifyEmbedURL,
            YoutubeEmbedURL
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING ArtistID
    """,
        artist.Title,
        artist.Country,
        artist.City,
        artist.StateCode,
        artist.YearFounded,
        artist.Description,
        str(artist.SpotifyEmbedURL) if artist.SpotifyEmbedURL else None,
        str(artist.YoutubeEmbedURL) if artist.YoutubeEmbedURL else None,
        connection=connection,
        cursor=cursor
    )
    return response[0]


# ArtistType Table
def post_artist_type(types: Optional[List[str]], artist_id: UUID, connection, cursor):
    if types:
        for type_ in types:
            execute(
            """
                INSERT INTO ArtistType (ArtistID, Type) 
                VALUES (%s, %s)
            """,
                (artist_id, type_),
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
                (artist_id, tag),
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
                (artist_id, social.SocialPlatform, social.Handle, str(social.Url)),
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
                (artist_id, image_id, index + 1),
                connection=connection,
                cursor=cursor
            )