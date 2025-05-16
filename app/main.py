from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from app.departments.router import router as department_router
from app.departments.employees.router import router as employee_router
from app.computers.router import router as computer_router
from app.usbs.router import router as usb_router
from app.events.router import router as event_router
from app.tasks.router import router as task_router


app = FastAPI()
add_pagination(app)


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

app.include_router(department_router)
app.include_router(computer_router)
app.include_router(usb_router)
app.include_router(employee_router)
app.include_router(event_router)
app.include_router(task_router)