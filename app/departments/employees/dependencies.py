from typing import Annotated

from fastapi import Query

from app.departments.employees.models import Employee


class EmployeesSearchArgsDepend:
    def __init__(
            self,
            department_id: Annotated[int, Query(ge=1)] = None,
            job_title: Annotated[str, Query(description='Должность (например, "Начальник", "Инженер")')] = None,
    ):
        self.department_id = department_id
        self.job_title = job_title

    @property
    def filters(self):
        filters = []
        if self.department_id:
            filters.append(Employee.department_id == self.department_id)
        if self.job_title:
            filters.append(Employee.job_title.icontains(self.job_title))

        return filters
