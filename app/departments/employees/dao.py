from app.dao.base import BaseDAO
from app.departments.employees.models import Employee


class ComputerDAO(BaseDAO):
    model = Employee
