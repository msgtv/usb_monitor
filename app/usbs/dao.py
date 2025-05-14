from app.dao.base import BaseDAO
from app.usbs.models import USB


class ComputerDAO(BaseDAO):
    model = USB
