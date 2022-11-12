from sqlalchemy import delete

from config import cfg


class RootMethods:
    async def create_me(self):
        async with cfg.db.async_session() as session:
            session.add(self)
            await session.commit()

    @staticmethod
    async def create_some(objects: list):
        async with cfg.db.async_session() as session:
            session.add_all(objects)
            await session.commit()

    @classmethod
    async def delete_all(cls):
        async with cfg.db.async_session() as session:
            sql = delete(cls)
            await session.execute(sql)
            await session.commit()
