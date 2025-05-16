from typing import List

from fastapi import APIRouter

from app.tasks.dao import TaskDAO
from app.tasks.schemas import STask

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)

@router.get('')
async def get_tasks() -> List[STask]:
    tasks = await TaskDAO.get_all()

    return tasks
