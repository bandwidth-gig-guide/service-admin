from app.db.connection import get_db_connection

def execute(query: str, values: tuple = (), connection=None, cursor=None):
    if connection and cursor:
        cursor.execute(query, values)
        result = cursor.fetchone()
        return result
    else:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()
                return cursor.fetchone()
