from typing import List

from fastapi import APIRouter

from app.usbs.dao import UsbDAO
from app.usbs.schemas import SUsb
from app.usbs.exceptions import UsbNotFoundException

router = APIRouter(
    prefix="/usbs",
    tags=["USB-устройства"],
)

@router.get('')
async def get_usbs() -> List[SUsb]:
    usbs = await UsbDAO().get_all()

    return usbs


@router.get('/{usb_id}')
async def get_usb(usb_id: int) -> SUsb:
    usb = await UsbDAO().get_by_id(usb_id)
    if usb:
        return usb
    raise UsbNotFoundException(f"No usb found with id {usb_id}")
