from app.dao.base import BaseDAO
from app.events.event_sources.models import EventSource


class ComputerDAO(BaseDAO):
    model = EventSource
