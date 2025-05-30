from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from typing import Annotated

from app.auth.dependencies import DefaultUser, ManagerUser, AdminUser, RootUser


router = APIRouter(
    prefix='',
    tags=['Фронтэнд'],
)


templates = Jinja2Templates(directory='app/templates')


@router.get('/', dependencies=[Depends(DefaultUser)])
async def get_main_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='main/main_page.html',
        context={'request': request},
    )

@router.get('/events', dependencies=[Depends(DefaultUser)])
async def get_events_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='events/main_page.html',
        context={'request': request},
    )


@router.get('/tasks', dependencies=[Depends(ManagerUser)])
async def get_tasks_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='tasks/main_page.html',
        context={'request': request},
    )

@router.get('/tasks/add', dependencies=[Depends(ManagerUser)])
async def get_tasks_add_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='tasks/add/main_page.html',
        context={'request': request},
    )

@router.get('/computers', dependencies=[Depends(DefaultUser)])
async def get_computers_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='computers/main_page.html',
        context={'request': request},
    )

@router.get('/computers/1', dependencies=[Depends(DefaultUser)])
async def get_computers_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='computers/computer/main_page.html',
        context={'request': request},
    )

@router.get('/usbs', dependencies=[Depends(DefaultUser)])
async def get_usbs_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='usbs/main_page.html',
        context={'request': request},
    )

@router.get('/employees', dependencies=[Depends(DefaultUser)])
async def get_employees_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='employees/main_page.html',
        context={'request': request},
    )

@router.get('/employees/1', dependencies=[Depends(DefaultUser)])
async def get_employees_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='employees/employee/main_page.html',
        context={'request': request},
    )
