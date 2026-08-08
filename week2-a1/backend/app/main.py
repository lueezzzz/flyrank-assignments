from fastapi import FastAPI, HTTPException, status
from app.api.routers import tasks

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health_check():
    return {"status": "ok"}

