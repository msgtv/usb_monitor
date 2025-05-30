import httpx

from app.auth.schemas import RefreshToken, Tokens, UserInDB


class AuthService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=base_url, timeout=httpx.Timeout(10))

    async def login(self, form_data):
        data = {
            "grant_type": form_data.grant_type,
            "username": form_data.username,
            "password": form_data.password,
            "scopes": form_data.scopes,
            "client_id": form_data.client_id,
            "client_secret": form_data.client_secret,
        }
        response = await self.client.post('/auth/token', data=data)

        if response.status_code == 200:
            return Tokens(**response.json())
        return None

    async def refresh_token(self, refresh_token: RefreshToken):
        response = await self.client.post('/auth/refresh', json=refresh_token.model_dump(mode='json'))

        if response.status_code == 200:
            return Tokens(**response.json())

        return None

    async def verify_token(self, token: str):
        headers = {'Authorization': f'Bearer {token}'}
        response = await self.client.get(
            "/users/me", 
            headers=headers,
        )

        if response.status_code == 200:
            return UserInDB(**response.json())
        return None
