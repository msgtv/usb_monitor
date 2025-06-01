import json
from datetime import datetime

import json
from datetime import datetime

import pytest
import redis.asyncio as redis
from sqlalchemy import insert
from httpx import AsyncClient, ASGITransport

from app.main import app as fastapi_app
from app.config import settings
from app.database import Base, async_session_maker, engine
from app.departments.models import Department
from app.comments.models import Comment
from app.computers.models import Computer
from app.departments.employees.models import Employee
from app.events.models import Event
from app.events.event_sources.models import EventSource
from app.tasks.models import Task
from app.usbs.models import USB



@pytest.fixture(autouse=True, scope="module")
async def prepare_database():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"app/tests/mock_data/mock_{model}.json", encoding='utf-8') as f:
            return json.load(f)
        
    departments = open_mock_json('departments')
    employees = open_mock_json('employees')
    computers = open_mock_json('computers')
    usbs = open_mock_json('usbs')
    event_sources = open_mock_json('event_sources')
    events = open_mock_json('events')
    tasks = open_mock_json('tasks')
    comments = open_mock_json('comments')
    

    async with async_session_maker() as s:
        add_departments = insert(Department).values(departments)
        add_employees = insert(Employee).values(employees)
        add_computers = insert(Computer).values(computers)
        add_usbs = insert(USB).values(usbs)
        add_event_sources = insert(EventSource).values(event_sources)
        add_events = insert(Event).values(events)
        add_tasks = insert(Task).values(tasks)
        add_comments = insert(Comment).values(comments)

        await s.execute(add_departments)
        await s.execute(add_employees)
        await s.execute(add_computers)
        await s.execute(add_usbs)
        await s.execute(add_event_sources)
        await s.execute(add_events)
        await s.execute(add_tasks)
        await s.execute(add_comments)
        
        await s.commit()


@pytest.fixture(scope='function')
async def ac():
    async with AsyncClient(
        transport=ASGITransport(app=fastapi_app),
        base_url="http://test/",
    ) as client:
        yield client


@pytest.fixture(scope='module')
async def session():
    async with async_session_maker() as session:
        yield session
