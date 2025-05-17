from typing import List, Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination import Page

from app.tasks.dao import TaskDAO, TaskDAODetailed
from app.tasks.schemas import STask, STaskDetail
from app.tasks.exceptions import TaskNotFound
from app.tasks.dependencies import TaskSearchArgsDepend, TaskDetailedSearchArgsDepend


router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)

@router.get('')
async def get_tasks(
        args: Annotated[TaskSearchArgsDepend, Depends(TaskSearchArgsDepend)]
) -> Page[STask]:
    tasks = await TaskDAO.get_all_paginated(args.filters)

    return tasks


@router.get('/detailed')
async def get_tasks_detailed(
        args: Annotated[TaskDetailedSearchArgsDepend, Depends(TaskDetailedSearchArgsDepend)]
) -> Page[STaskDetail]:
    return await TaskDAODetailed.get_all_paginated(args.filters)


@router.get('/{task_id}')
async def get_task_by_id(task_id: int) -> STaskDetail:
    task = await TaskDAO.get_by_id(task_id)
    if task:
        return task
    raise TaskNotFound(f"No task found with id {task_id}")
