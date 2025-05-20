from typing import Annotated

from fastapi import APIRouter, Depends, Path
from fastapi_pagination import Page

from app.dependencies import SessionDepend
from app.usbs.dao import UsbDAO, UsbDetailedDAO
from app.usbs.schemas import SUsb, SUsbDetail, SUsbDetailedData
from app.usbs.exceptions import UsbNotFoundException, UsbOrDepartmentNotFoundException
from app.usbs.dependencies import UsbSearchArgsDepend, UsbManageArgsDepend


router = APIRouter(
    prefix="/usbs",
    tags=["USB-устройства"],
)


@router.get('')
async def get_usbs(
        args: Annotated[UsbSearchArgsDepend, Depends(UsbSearchArgsDepend)],
        session: SessionDepend,
) -> Page[SUsb]:
    return await UsbDAO.get_all_paginated(session=session, filters=args.filters)


@router.get('/detailed')
async def get_usb_detailed(
        args: Annotated[UsbSearchArgsDepend, Depends(UsbSearchArgsDepend)],
        session: SessionDepend,
) -> Page[SUsbDetail]:
    return await UsbDAO.get_all_paginated(session=session, filters=args.filters)


@router.get('/{usb_id}')
async def get_usb(
        usb_id: Annotated[int, Path(ge=1)],
        session: SessionDepend,
) -> SUsbDetailedData:
    usb = await UsbDetailedDAO().get_by_id(session=session, obj_id=usb_id)
    if usb:
        return usb
    raise UsbNotFoundException(f"No usb found with id {usb_id}")


@router.patch('/{usb_id}')
async def patch_usb(
        args: Annotated[UsbManageArgsDepend, Depends(UsbManageArgsDepend)],
        session: SessionDepend,
) -> SUsb:
    usb = await UsbDAO().update(session=session, usb_id=args.usb_id, **args.values)

    if usb:
        return usb
    if args.values.get('department_id'):
        raise UsbOrDepartmentNotFoundException(
            detail=f'No usb with id {args.usb_id} '
                   f'or department with id {args.department_id} found'
        )
    raise UsbNotFoundException(f'No usb with id {args.usb_id} found')
