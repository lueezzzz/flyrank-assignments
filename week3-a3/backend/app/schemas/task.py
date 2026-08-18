from pydantic import BaseModel, Field

class CreateTask(BaseModel):
    title: str = Field(min_length=1, max_length=20)
    description: str | None = None


class UpdateTask(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=20)
    description: str | None = None
    is_completed: bool | None = None


class Task(BaseModel):
    id: int
    title: str
    description: str | None
    is_completed: bool
