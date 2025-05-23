from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix='',
    tags=['Фронтэнд'],
)


templates = Jinja2Templates(directory='app/templates')


@router.get('/')
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

@router.get('/computers/1')
async def get_computers_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='computers/computer/main_page.html',
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

@router.get('/employees/1')
async def get_employees_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='employees/employee/main_page.html',
        context={'request': request},
    )
