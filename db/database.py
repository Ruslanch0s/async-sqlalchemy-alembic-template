from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class AsyncDatabaseSession:
    def __init__(self):
        self._engine = create_async_engine(
            "postgresql+asyncpg://postgres:bezeq123@localhost:5432/postgres",
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


async_db_session = AsyncDatabaseSession()
