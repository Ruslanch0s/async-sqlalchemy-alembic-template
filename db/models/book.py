from sqlalchemy import Column, Integer, String, select

from config import cfg
from db.database import Base
from db.root_methods import RootMethods


class Book(Base, RootMethods):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    market = Column(String(length=100))
    name = Column(String(length=100))

    def __init__(self, market: str, name: str):
        self.market = market
        self.name = name

    @classmethod
    async def get_all_markets(cls):
        """
        :return: (['market'],)
        """
        async with cfg.db.async_session() as session:
            sql = select(cls.market).distinct(cls.market)
            result = await session.execute(sql)
        return result.fetchall()

    @classmethod
    async def get_market_books(cls, market: str):
        async with cfg.db.async_session() as session:
            sql = select(cls).where(cls.market == market)
            result = await session.execute(sql)
        return result.fetchall()
