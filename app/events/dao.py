from app.dao.base import BaseDAO
from app.events.models import Event


class EventDAO(BaseDAO):
    model = Event
