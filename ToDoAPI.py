
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str = "-"
    done: bool = False
    created_at: datetime

@app.get("/tasks")
def get_tasks():
    return {"tasks":  Task}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"id": task_id}

@app.post("/tasks")
def create_task(task: Task):
    return {"message": "Task created"}

@app.post("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task": Task.tasks[task_id]}

@app.delete("/tasks/{task_id}")
def delete_task(id: int):
    return {"id": id}

#ddfd