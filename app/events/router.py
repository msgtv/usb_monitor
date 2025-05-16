from typing import List

from fastapi import APIRouter
from fastapi_pagination import Page

from app.events.dao import EventDAO
from app.events.schemas import SEvent

router = APIRouter(
    prefix="/events",
    tags=["События SNS"],
)

@router.get('')
async def get_events() -> Page[SEvent]:
    events = await EventDAO.get_all_paginated()

    return events
