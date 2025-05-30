from typing import Annotated

from fastapi import Depends, HTTPException, Cookie, status
from fastapi.security import OAuth2PasswordBearer

from app.auth.schemas import UserInDB, oauth2_scheme
from app.auth.service import AuthService
from app.config import settings

auth_service = AuthService(base_url=settings.AUTH_SERVER_URL)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> UserInDB:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = await auth_service.verify_token(token)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


CurrentUser = Annotated[UserInDB, Depends(get_current_user)] 