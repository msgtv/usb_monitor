from typing import List, Annotated, Union

from fastapi import APIRouter, Depends
from fastapi_pagination import Page

from app.computers.dao import ComputerDAO, ComputerDAODetailed
from app.computers.schemas import SComputer, SComputerDetail
from app.computers.exceptions import ComputerNotFoundException
from app.computers.dependencies import ComputersSearchArgsDepend, ComputerPatchArgsDepend

router = APIRouter(
    prefix="/computers",
    tags=["Компьютеры"],
)

@router.get('')
async def get_computers(
        args: Annotated[ComputersSearchArgsDepend, Depends(ComputersSearchArgsDepend)]
) -> Page[SComputer]:
    computers = await ComputerDAO.get_all_paginated(args.filters)

    return computers


@router.get('/detailed')
async def get_computers_detailed(
        args: Annotated[ComputersSearchArgsDepend, Depends(ComputersSearchArgsDepend)]
) -> Page[SComputerDetail]:
    computers = await ComputerDAODetailed.get_all_paginated(args.filters)

    return computers


@router.get('/{computer_id}')
async def get_computer_by_id(computer_id: int) -> SComputerDetail:
    computer = await ComputerDAODetailed.get_by_id(computer_id)

    if computer:
        return computer
    raise ComputerNotFoundException(f"No computer with id {computer_id}")


@router.patch('/{computer_id}')
async def patch_computer(
        args: Annotated[ComputerPatchArgsDepend, Depends(ComputerPatchArgsDepend)]
) -> SComputer:
    computer = await ComputerDAO.update(object_id=args.computer_id, **args.values)
    if computer:
        return computer
    raise ComputerNotFoundException(f"No computer with id {args.computer_id}")
