from app.db.db import get_connection
from app.schemas.task import CreateTask, UpdateTask


def get_tasks() -> list[dict]:
    connection = get_connection()
    try:
        tasks = connection.execute("""
            SELECT id, title, description, is_completed FROM tasks 
            ORDER by id

        """).fetchall()

        return [dict(t) for t in tasks]
    finally:
        connection.close()


def get_task(task_id: int) -> dict:
    connection = get_connection()

    try:
        task = connection.execute(
            """
            SELECT id, title, description, is_completed FROM tasks
            WHERE id = ?
        """,
            (task_id,),
        ).fetchone()

        if not task:
            return None

        return dict(task)
    finally:
        connection.close()


def update_task(task_id: int, task: UpdateTask) -> dict:

    existing_task = get_task(task_id)

    if existing_task is None:
        return None

    title = task.title if task.title is not None else existing_task["title"]
    description = task.description if "description" in task.model_fields_set else existing_task["description"]
    is_completed = task.is_completed if task.is_completed is not None else existing_task["is_completed"]

    connection = get_connection()
    try:
        connection.execute(
            """
        UPDATE tasks
        SET title = ?, description = ?, is_completed = ?
        WHERE id = ?
        """,
            (title, description, is_completed, task_id),

        )

        connection.commit()

        updated_task = connection.execute(
            """
            SELECT id, title, description, is_completed FROM tasks
            WHERE id = ?
            """, (task_id,),
        ).fetchone()

        if updated_task is None:
            return None

        return dict(updated_task)

        
    finally:
        connection.close()


def create_task(task: CreateTask) -> dict:
    connection = get_connection()

    try:
        new_task = connection.execute(
            """
            INSERT into tasks (title, description)
            VALUES (?, ?)
            """,
            (task.title, task.description),
        )

        connection.commit()

        created_task = connection.execute(
            """
            SELECT id, title, description, is_completed FROM tasks
            WHERE id = ?
            """,
            (new_task.lastrowid,),
        ).fetchone()

        return dict(created_task)

    finally:
        connection.close()


def delete_task(task_id: int) -> None:
    connection = get_connection()
    try:
        removed_task = connection.execute(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        connection.commit()

        return removed_task.rowcount > 0

    finally:
        connection.close()
