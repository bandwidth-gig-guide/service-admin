from app.query.execute_with_return import execute as execute_with_return
from app.db.connection import get_db_connection
from psycopg2 import DatabaseError

from app.rest.artist.secondary_tables.post_artist_type import post_artist_type
from app.rest.artist.secondary_tables.post_artist_tag import post_artist_tag
from app.rest.artist.secondary_tables.post_artist_social import post_artist_social
from app.rest.artist.secondary_tables.post_artist_image import post_artist_image

from app.model.artist_insert import ArtistInsert
from uuid import UUID


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