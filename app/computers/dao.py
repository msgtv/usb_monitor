from app.dao.base import BaseDAO
from app.computers.models import Computer


class ComputerDAO(BaseDAO):
    model = Computer
