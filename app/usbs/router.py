from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination import Page

from app.usbs.dao import UsbDAO
from app.usbs.schemas import SUsb, SUsbDetail, SUsbDetailedData
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
    return await UsbDAO.get_all_paginated(args.filters)


@router.get('/detailed')
async def get_usb_detailed(
        args: Annotated[UsbSearchArgsDepend, Depends(UsbSearchArgsDepend)]
) -> Page[SUsbDetail]:
    return await UsbDAO.get_all_paginated(args.filters)


@router.get('/{usb_id}')
async def get_usb(usb_id: int) -> SUsbDetailedData:
    usb = await UsbDAO().get_by_id(usb_id)
    if usb:
        return usb
    raise UsbNotFoundException(f"No usb found with id {usb_id}")
