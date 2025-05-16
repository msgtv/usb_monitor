from fastapi import Query


class EmployeesSearchArgsDepend:
    def __init__(
            self,
            department_id: int = Query(None, gt=0),
            job_title: str = Query(None, description='Должность (например, "Начальник", "Инженер")'),
    ):
        self.department_id = department_id
        self.job_title = job_title
