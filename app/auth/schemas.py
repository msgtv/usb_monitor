from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


class AccessToken(BaseModel):
    access_token: str

class RefreshToken(BaseModel):
    refresh_token: str

class Tokens(AccessToken, RefreshToken):
    token_type: str = "Bearer"


class UserInDB(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    role_id: int
    role_name: str
