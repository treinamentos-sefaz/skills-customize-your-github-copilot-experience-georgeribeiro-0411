import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: list[Task] = [
    Task(id=1, title="Read the API documentation"),
    Task(id=2, title="Build a REST endpoint", completed=True),
]
next_task_id = 3


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)