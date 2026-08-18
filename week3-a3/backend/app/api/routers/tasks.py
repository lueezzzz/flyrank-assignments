from fastapi import APIRouter, HTTPException, status
from app.schemas.task import Task, CreateTask, UpdateTask
from app.api.repository import repository_tasks

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.get("/", response_model=list[Task], status_code=status.HTTP_200_OK)
def get_tasks() -> list[dict]:
    return repository_tasks.get_tasks()

@router.get("/{task_id}", response_model=Task, status_code=status.HTTP_200_OK )
def get_task(task_id: int) -> dict:
    task = repository_tasks.get_task(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} does not exist",
        )
    return task


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: CreateTask) -> dict:
    return repository_tasks.create_task(task)

@router.patch("/{task_id}", response_model=Task)
def update_task(task_id: int, update: UpdateTask) -> dict:
    updated_task = repository_tasks.update_task(task_id, update)
    if updated_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    deleted = repository_tasks.delete_task(task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )


# @router.get("/{task_id}", status_code=status.HTTP_200_OK)
# def get_task(task_id: int):
#     for task in tasks:
#         if task.id == task_id:
#             return task
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found"
#     )


# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create_task(task: Task):
#     if not task.title or task.title.strip() == "":
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="Title is missing or empty"
#         )

#     next_id = 1 if len(tasks) == 0 else tasks[-1].id + 1
#     new_task = Task(id=next_id, title=task.title, done=False)
#     tasks.append(new_task)

#     return new_task


# @router.put("/{task_id}")
# def update_task(task_id: int, title: str, done: bool):
#     if title is None and done is False:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Request cannot be empty or invalid",
#         )

#     for task in tasks:
#         if task.id == task_id:
#             task.title = title
#             task.done = done
#             return task

#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found"
#     )


# @router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_task(task_id: int):
#     for task in tasks:
#         if task.id == task_id:
#             tasks.remove(task)
#             return

#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found"
#     )
