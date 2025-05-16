from typing import List, Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination import Page, LimitOffsetParams

from app.usbs.dao import UsbDAO
from app.usbs.schemas import SUsb
from app.usbs.exceptions import UsbNotFoundException
from app.usbs.dependencies import UsbSearchArgsDepend

router = APIRouter(
    prefix="/usbs",
    tags=["USB-устройства"],
)

@router.get('')
async def get_usbs(
        args: Annotated[UsbSearchArgsDepend, Depends(UsbSearchArgsDepend)]
) -> Page[SUsb]:
    params = {}
    if args.is_accepted is not None:
        params['is_accepted'] = args.is_accepted
    if args.department_id is not None:
        params['department_id'] = args.department_id

    if args.class_types:
        usbs = await UsbDAO.get_usbs_by_class_type(args.class_types, **params)
    else:
        usbs = await UsbDAO.get_all_paginated(**params)

    return usbs


@router.get('/{usb_id}')
async def get_usb(usb_id: int) -> SUsb:
    usb = await UsbDAO().get_by_id(usb_id)
    if usb:
        return usb
    raise UsbNotFoundException(f"No usb found with id {usb_id}")
