from typing import List

from fastapi import APIRouter
from fastapi_pagination import Page

from app.tasks.dao import TaskDAO
from app.tasks.schemas import STask

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)

@router.get('')
async def get_tasks() -> Page[STask]:
    tasks = await TaskDAO.get_all_paginated()

    return tasks
