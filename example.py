import asyncio

from sqlalchemy.orm import Query

from db.database import async_db_session
from db.models.book import Book


async def async_main():
    await async_db_session.drop_all_tables()
    await async_db_session.create_all_tables()

    b1 = Book(market='читай город', name='тайная комната')
    await b1.create_me()

    b1 = Book(market='читай город', name='артур и лилипуты')
    b2 = Book(market='литрес', name='тайная комната')
    await Book.create_some([b1, b2])

    print(await Book.get_all_markets())
    books = await Book.get_market_books(market='читай город')
    for row in books:
        book = row[0]
        print(book.name, ':', book.market)


if __name__ == '__main__':
    asyncio.run(async_main())
