from datetime import datetime
from typing import Annotated

from sqlalchemy import NullPool, sql, func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
    sessionmaker,
)


from app.config import settings


if settings.MODE == 'TEST':
    DATABASE_URL = (
        f'postgresql+asyncpg://'
        f'{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@'
        f'{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}')
    params = {'poolclass': NullPool}
else:
    DATABASE_URL = (
        f'postgresql+asyncpg://'
        f'{settings.TEST_POSTGRES_USER}:'
        f'{settings.TEST_POSTGRES_PASSWORD}@'
        f'{settings.TEST_POSTGRES_HOST}:'
        f'{settings.TEST_POSTGRES_PORT}'
    )
    params = {}


engine = create_async_engine(DATABASE_URL, **params)

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# настройка аннотаций
int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.utcnow)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]
int_null_true = Annotated[int, mapped_column(nullable=True)]
bool_default_false = Annotated[bool, mapped_column(server_default=sql.false(), default=False)]


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int_pk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    is_deleted: Mapped[bool_default_false]
