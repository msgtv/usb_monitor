from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination

from app.departments.router import router as department_router
from app.departments.employees.router import router as employee_router
from app.computers.router import router as computer_router
from app.usbs.router import router as usb_router
from app.events.router import router as event_router
from app.tasks.router import router as task_router
from app.pages.router import router as page_router
from app.comments.router import router as comment_router


app = FastAPI()
app.mount(
    '/static',
    StaticFiles(directory='app/static'),
    name='static',
)


ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Authorization",
    ],
)

api_router = APIRouter(prefix="/api/v1")


api_router.include_router(department_router)
api_router.include_router(computer_router)
api_router.include_router(usb_router)
api_router.include_router(employee_router)
api_router.include_router(event_router)
api_router.include_router(task_router)
api_router.include_router(comment_router)
app.include_router(api_router)
app.include_router(page_router)

add_pagination(app)
