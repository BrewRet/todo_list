from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


tasks = []


class PostTask(BaseModel):
    title: str
    description: str


app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello World"
    }

@app.get("/tasks")
async def get_tasks():
    global tasks
    return {
        "tasks":  tasks
    }


@app.get("tasks/{id}")
async def get_task_by_id(id:int):
    global tasks
    try:
        task = tasks[id]
        return {id: task}
    except IndexError:
        raise HTTPException(404, f"Task by this id: {id}, not found")


@app.post("/tasks")
async def post_task(task: PostTask):
    pass

