from typing import List

from fastapi import APIRouter

from app.computers.dao import ComputerDAO
from app.computers.schemas import SComputer
from app.computers.exceptions import ComputerNotFoundException


router = APIRouter(
    prefix="/computers",
    tags=["Компьютеры"],
)

@router.get('')
async def get_computers() -> List[SComputer]:
    computers = await ComputerDAO().get_all()

    return computers

@router.get('/{computer_id}')
async def get_computer_by_id(computer_id: int) -> SComputer:
    computer = await ComputerDAO().get_by_id(computer_id)

    if computer:
        return computer
    raise ComputerNotFoundException(f"No computer with id {computer_id}")


