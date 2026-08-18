import sqlite3

def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect('tasks.db')
    connection.row_factory = sqlite3.Row
    return connection

def init_db() -> None:
    connection = get_connection()

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                is_completed BOOLEAN NOT NULL DEFAULT 0
            )
            """
        )
        connection.commit()
    finally:
        connection.close()




