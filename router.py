from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends

from repository import TaskRepository
from schemas import STaskAdd


router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks():
    tasks = await TaskRepository.get_all()
    return {"tasks": tasks}
