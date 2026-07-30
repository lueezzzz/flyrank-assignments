from fastapi import APIRouter, HTTPException, status
from app.schemas.task import Task
from app.db.mock_db import tasks

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.get("/")
def get_tasks():
    return tasks


@router.get("/{task_id}", status_code=status.HTTP_200_OK)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found"
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    if not task.title or task.title.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Title is missing or empty"
        )

    next_id = 1 if len(tasks) == 0 else tasks[-1].id + 1
    new_task = Task(id=next_id, title=task.title, done=False)
    tasks.append(new_task)

    return new_task


@router.put("/{task_id}")
def update_task(task_id: int, title: str, done: bool):
    if title is None and done is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Request cannot be empty or invalid",
        )

    for task in tasks:
        if task.id == task_id:
            task.title = title
            task.done = done
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found"
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found"
    )
