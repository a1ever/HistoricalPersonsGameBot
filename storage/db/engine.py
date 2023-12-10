from typing import Union

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


def create_pool(url: Union[URL, str]) -> AsyncEngine:
    return create_async_engine(url=url)


async def proceed_schemas(engine: AsyncEngine, metadata) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, class_=AsyncSession)
