from db.database import async_db_session


class RootMethods:
    async def create_me(self):
        async with async_db_session() as session:
            session.add(self)
            await session.commit()

    @staticmethod
    async def create_some(objects: list):
        async with async_db_session() as session:
            session.add_all(objects)
            await session.commit()
