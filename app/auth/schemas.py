from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


class AccessToken(BaseModel):
    access_token: str

class RefreshToken(BaseModel):
    refresh_token: str

class Tokens(AccessToken, RefreshToken):
    token_type: str = "Bearer"


class UserInDB(BaseModel):
    username: str
    first_name: str
    last_name: str
    role: str
