from typing import List, Annotated, Union

from fastapi import APIRouter, Depends
from fastapi_pagination import Page

from app.computers.dao import ComputerDAO
from app.computers.schemas import SComputer, SComputerDetail
from app.computers.exceptions import ComputerNotFoundException
from app.computers.dependencies import ComputersSearchArgsDepend


router = APIRouter(
    prefix="/computers",
    tags=["Компьютеры"],
)

@router.get('')
async def get_computers(
        args: Annotated[ComputersSearchArgsDepend, Depends(ComputersSearchArgsDepend)]
) -> Page[SComputer]:
    params = {}
    if args.department_id:
        params["department_id"] = args.department_id
    if args.is_accepted_usb:
        params["is_accepted_usb"] = args.is_accepted_usb

    computers = await ComputerDAO.get_all_paginated(**params)

    return computers


@router.get('/detailed')
async def get_computers_detailed(
        args: Annotated[ComputersSearchArgsDepend, Depends(ComputersSearchArgsDepend)]
) -> Page[SComputerDetail]:
    params = {}
    if args.department_id:
        params["department_id"] = args.department_id
    if args.is_accepted_usb:
        params["is_accepted_usb"] = args.is_accepted_usb


    computers = await ComputerDAO.get_all_detailed_paginated(**params)

    return computers


@router.get('/{computer_id}')
async def get_computer_by_id(computer_id: int) -> SComputerDetail:
    computer = await ComputerDAO.get_by_id_detail(computer_id)

    if computer:
        return computer
    raise ComputerNotFoundException(f"No computer with id {computer_id}")


