from typing import List, Annotated

from fastapi import APIRouter, Depends, Path
from fastapi_pagination import Page

from app.dependencies import SessionDepend
from app.tasks.dao import TaskDAO, TaskDAODetailed
from app.tasks.schemas import STask, STaskDetail
from app.tasks.exceptions import TaskNotFound, ComputerOrUsbNotFound
from app.tasks.dependencies import TaskSearchArgsDepend, TaskDetailedSearchArgsDepend, TaskAddArgsDepend
from app.auth.dependencies import DefaultUser, ManagerUser, AdminUser, RootUser

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)

@router.get('', dependencies=[Depends(DefaultUser)])
async def get_tasks(
        args: Annotated[TaskSearchArgsDepend, Depends(TaskSearchArgsDepend)],
        session: SessionDepend,
) -> Page[STask]:
    tasks = await TaskDAO.get_all_paginated(session=session, filters=args.filters)
    return tasks


@router.get('/detailed', dependencies=[Depends(ManagerUser)])
async def get_tasks_detailed(
        args: Annotated[TaskDetailedSearchArgsDepend, Depends(TaskDetailedSearchArgsDepend)],
        session: SessionDepend,
) -> Page[STaskDetail]:
    return await TaskDAODetailed.get_all_paginated(session=session, filters=args.filters)


@router.get('/{task_id}', dependencies=[Depends(DefaultUser)])
async def get_task_by_id(
        task_id: Annotated[int, Path(ge=1)],
        session: SessionDepend,
) -> STaskDetail:
    task = await TaskDAODetailed.get_by_id(session=session, obj_id=task_id)
    if task:
        return task
    raise TaskNotFound(f"No task found with id {task_id}")


@router.post('/add', dependencies=[Depends(ManagerUser)])
async def add_task(
        args: Annotated[TaskAddArgsDepend, Depends(TaskAddArgsDepend)],
        session: SessionDepend,
) -> STask:
    task = await TaskDAO.add(session=session, **args.values)
    if task:
        return task

    raise ComputerOrUsbNotFound(detail=f'No Computer id {args.computer_id} or Usb id {args.usb_id} found!')


@router.patch('/{task_id}/close', dependencies=[Depends(ManagerUser)])
async def close_task(
        task_id: Annotated[int, Path(ge=1)],
        session: SessionDepend,
):
    task = await TaskDAO.update(session=session, obj_id=task_id, is_completed=True)
    if task:
        return task
    raise TaskNotFound(detail=f"No task found with id {task_id}")
