from fastapi import FastAPI, HTTPException, status

app = FastAPI()

class Task:
    def __init__(self, id: int, title: str, done: bool):
        self.id = id
        self.title = title
        self.done = done

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
