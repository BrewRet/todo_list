from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services.task_service import (
    get_all_tasks,
    get_task_by_id,
    add_task_by_id,
    change_task_by_id,
    delete_task_by_id,
)




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
    tasks = await get_all_tasks()
    return {
        "tasks": tasks
    }


@app.get("/tasks/{id}")
async def show_task_by_id(id:int):
    try:
        task = await get_task_by_id(id)
        return {id: task}
    except IndexError:
        raise HTTPException(404, f"Task by this id: {id}, not found")


@app.post("/tasks")
async def add_task(task: RequestTask):
    await add_task_by_id(**task)
    return {"result": "Task added"}


@app.put("/tasks/{id}")
async def change_task(id:int, task: RequestTask):
    try: 
        await change_task_by_id(id, **task)
    except IndexError:
        raise HTTPException(404, f"Task by this id: {id}, not found")
    return {"result": "Success"}


@app.delete("/tasks/{id}")
async def delete_task(id:int):

    try:
        await delete_task_by_id(id)
    except IndexError:
        raise HTTPException(404, f"Task by this id: {id}, not found")
    return {"result": "Task deleted"}