from app.query.execute import execute
from app.db.connection import get_db_connection
from psycopg2 import DatabaseError

from app.rest.artist.secondary_tables.put_artist_type import put_artist_type
from app.rest.artist.secondary_tables.put_artist_tag import put_artist_tag
from app.rest.artist.secondary_tables.put_artist_social import put_artist_social
from app.rest.artist.secondary_tables.put_artist_image import put_artist_image

from app.model.artist_insert import ArtistInsert
from uuid import UUID


def put(artist_id: UUID, artist: ArtistInsert):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                update_artist(artist_id, artist, connection, cursor)
                put_artist_type(artist.Types, artist_id, connection, cursor)
                put_artist_tag(artist.Tags, artist_id, connection, cursor)
                put_artist_social(artist.Socials, artist_id, connection, cursor)
                put_artist_image(artist.Images, artist_id, connection, cursor)
                connection.commit()
                return artist_id
            except DatabaseError:
                connection.rollback()
                raise


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
