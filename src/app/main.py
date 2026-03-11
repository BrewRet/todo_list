from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


tasks = []


class RequestTask(BaseModel):
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
async def post_task(task: RequestTask):
    global tasks
    tasks.append((task.title, task.description))
    return {"result": "Task added"}


@app.put("/tasks/{id}")
async def change_task(id:int, task: RequestTask):
    global tasks
    try: 
        tasks[id] = (task.title, task.description)
    except IndexError:
        raise HTTPException(404, f"Task by this id: {id}, not found")
    return {f"task {id}": task[id]}


@app.delete("/tasks/{id}")
async def delete_task(id):
    global tasks
    try:
        tasks.pop(id)
    except IndexError:
        raise HTTPException(404, f"Task by this id: {id}, not found")
    return {"result": "Task deleted"}