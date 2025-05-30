from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.dependencies import auth_service, CurrentUser
from app.auth.schemas import AccessToken, Tokens, RefreshToken, UserInDB, oauth2_scheme

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Tokens:
    if not form_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No credentials provided",
        )

    tokens = await auth_service.login(form_data)
    if not tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    return tokens


@router.post("/refresh")
async def refresh_token(
    refresh_token: RefreshToken,
) -> Tokens:
    tokens = await auth_service.refresh_token(refresh_token)
    if not tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )
    
    return tokens


@router.post("/logout")
async def logout(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> None:
    await auth_service.logout(token)


@router.get("/me")
async def me(
    user: CurrentUser,
) -> UserInDB:
    return user