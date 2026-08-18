from app.db.db import get_connection
from app.schemas.task import CreateTask, UpdateTask


def get_tasks() -> list[dict]:
    with get_connection() as connection:
        tasks = connection.execute("""
            SELECT id, title, description, is_completed FROM tasks 
            ORDER by id
        """).fetchall()
        return tasks


def get_task(task_id: int) -> dict | None:
    with get_connection() as connection:
        task = connection.execute(
            """
            SELECT id, title, description, is_completed FROM tasks
            WHERE id = %s
        """,
            (task_id,),
        ).fetchone()
        return task


def update_task(task_id: int, task: UpdateTask) -> dict | None:

    existing_task = get_task(task_id)

    if existing_task is None:
        return None

    title = task.title if task.title is not None else existing_task["title"]
    description = task.description if "description" in task.model_fields_set else existing_task["description"]
    is_completed = task.is_completed if task.is_completed is not None else existing_task["is_completed"]

  
    with get_connection() as connection:
        updated_task = connection.execute(
            """
            UPDATE tasks
            SET title = %s, description = %s, is_completed = %s
            WHERE id = %s
            RETURNING id, title, description, is_completed
            """,
            (title, description, is_completed, task_id),
        ).fetchone()

        return updated_task


def create_task(task: CreateTask) -> dict:
    connection = get_connection()

    with get_connection() as connection:
        new_task = connection.execute(
            """
            INSERT into tasks (title, description)
            VALUES (%s, %s)
            RETURNING id, title, description, is_completed
            """,
            (task.title, task.description),
        ).fetchone()

        return new_task



def delete_task(task_id: int) -> bool:
    connection = get_connection()
    with get_connection() as connection:
        removed_task = connection.execute(
            """
            DELETE FROM tasks
            WHERE id = %s
            """,
            (task_id,),
        )   
        return removed_task.rowcount > 0

