from app.dao.base import BaseDAO
from app.departments.models import Department


class DepartmentDAO(BaseDAO):
    model = Department
