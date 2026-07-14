from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Task(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    done: bool = False

tasks = [
    Task(id=1, title="Buy groceries", done=False),
    Task(id=2, title="Finish FastAPI tutorial", done=True),
    Task(id=3, title="Clean the room", done=False),
] 

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health_check():
    return {"status": "ok"} 


@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found"
    )


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):

    if not task.title or task.title.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Title is missing or empty"
        )

    if len(tasks) == 0:
        next_id = 1
    else:
        next_id = tasks[-1].id + 1

    new_task = Task(id=next_id, title=task.title, done=False)

    tasks.append(new_task)

    return new_task
