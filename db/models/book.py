from sqlalchemy import Column, Integer, String

from db.database import async_db_session, Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)

    def __init__(self, name: str):
        self.name = name

    async def create_me(self):
        async with async_db_session() as session:
            session.add(self)
            await session.commit()

    @staticmethod
    async def create_some(objects: list):
        async with async_db_session() as session:
            session.add_all(objects)
            await session.commit()
