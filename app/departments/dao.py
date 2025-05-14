from app.dao.base import BaseDAO
from app.departments.models import Department


class ComputerDAO(BaseDAO):
    model = Department
