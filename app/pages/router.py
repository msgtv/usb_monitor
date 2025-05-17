from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

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
async def get_events_page(
        request: Request,
):
    return templates.TemplateResponse(
        name='tasks/main_page.html',
        context={'request': request},
    )
