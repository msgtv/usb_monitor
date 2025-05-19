from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi_pagination import Page, Params
from fastapi_pagination.api import pagination_ctx

from app.events.router import get_events_detailed

router = APIRouter(
    prefix='/pages',
    tags=['Фронтэнд'],
)


templates = Jinja2Templates(directory='app/templates')


@router.get('/main')
async def get_main_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='main/main_page.html',
        context={'request': request},
    )

@router.get('/events')
async def get_events_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='events/main_page.html',
        context={'request': request},
    )


@router.get('/tasks')
async def get_tasks_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='tasks/main_page.html',
        context={'request': request},
    )

@router.get('/tasks/add')
async def get_tasks_add_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='tasks/add/main_page.html',
        context={'request': request},
    )

@router.get('/computers')
async def get_computers_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='computers/main_page.html',
        context={'request': request},
    )

@router.get('/usbs')
async def get_usbs_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='usbs/main_page.html',
        context={'request': request},
    )

@router.get('/employees')
async def get_employees_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='employees/main_page.html',
        context={'request': request},
    )
