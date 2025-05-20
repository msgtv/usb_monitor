from typing import List, Annotated

from fastapi import APIRouter, Depends, Path
from fastapi_pagination import Page

from app.tasks.dao import TaskDAO, TaskDAODetailed
from app.tasks.models import Task
from app.tasks.schemas import STask, STaskDetail
from app.tasks.exceptions import TaskNotFound, ComputerOrUsbNotFound
from app.tasks.dependencies import TaskSearchArgsDepend, TaskDetailedSearchArgsDepend, TaskAddArgsDepend

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
    task = await TaskDAODetailed.get_by_id(task_id)
    if task:
        return task
    raise TaskNotFound(f"No task found with id {task_id}")


@router.post('/add')
async def add_task(
        args: Annotated[TaskAddArgsDepend, Depends(TaskAddArgsDepend)],
) -> STask:
    task = await TaskDAO.add(**args.values)
    if task:
        return task

    raise ComputerOrUsbNotFound(detail=f'No Computer id {args.computer_id} or Usb id {args.usb_id} found!')


@router.patch('/{task_id}/close')
async def close_task(
        task_id: int,
):
    task = await TaskDAO.update(task_id, is_completed=True)
    if task:
        return task
    raise TaskNotFound(detail=f"No task found with id {task_id}")
