import os
import psycopg
from psycopg.rows import dict_row

def get_connection() -> psycopg.Connection:
    return psycopg.connect(
        os.getenv("DATABASE_URL", "postgres://postgres:dev@db:5432/tasks"),
        row_factory = dict_row
    )

def init_db() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                is_completed BOOLEAN NOT NULL DEFAULT FALSE
            )
            """
        )

        row = connection.execute("SELECT COUNT(*) AS count FROM tasks").fetchone()
        if row["count"] == 0:
            connection.execute(
                """
                INSERT INTO tasks (title, is_completed) VALUES
                    (%s, %s),
                    (%s, %s),
                    (%s, %s)
                """,
                (
                    "Setup environment", True,
                    "Connect database", False,
                    "Build API endpoints", False
                )
            )