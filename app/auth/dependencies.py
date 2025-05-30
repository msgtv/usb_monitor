from typing import Annotated, Callable
from functools import wraps

from fastapi import Depends, HTTPException, Cookie, status
from fastapi.security import OAuth2PasswordBearer

from app.auth.schemas import UserInDB, oauth2_scheme
from app.auth.service import AuthService
from app.config import settings

auth_service = AuthService(base_url=settings.AUTH_SERVER_URL)


def get_current_user(min_role_id: int = 1):
    async def current_user(
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
            
        if user.role_id < min_role_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Недостаточно прав для выполнения операции"
            )
            
        return user
    
    return current_user


DefaultUser = get_current_user(min_role_id=1)
ManagerUser = get_current_user(min_role_id=2)
AdminUser = get_current_user(min_role_id=3)
RootUser = get_current_user(min_role_id=4)