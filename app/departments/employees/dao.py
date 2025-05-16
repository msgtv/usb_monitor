from app.dao.base import BaseDAO
from app.departments.employees.models import Employee


class EmployeeDAO(BaseDAO):
    model = Employee
