

tasks = []


async def get_all_tasks() -> list[tuple[str]]:
    global tasks
    return tasks


async def get_task_by_id(id: int) -> tuple[str]:
    global tasks
    return tasks[id]


async def add_task_by_id(title: str, description: str) -> None:
    global tasks
    tasks.append((title, description))


async def change_task_by_id(id: int, title: str, description: str) -> None:
    global tasks
    tasks[id] = (title, description)


async def delete_task_by_id(id: int) -> None:
    global tasks
    tasks.pop(id) 