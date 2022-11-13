from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base


class AsyncDatabaseSession:
    def __init__(self, url):
        self._engine = create_async_engine(
            url,
            echo=False,
            future=True
        )
        self._async_db_session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )

    async def create_all_tables(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_all_tables(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    def __call__(self, *args, **kwargs):
        return self._async_db_session()
