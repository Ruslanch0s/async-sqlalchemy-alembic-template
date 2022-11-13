import asyncio

from config import cfg
from db.models.book import Book


async def async_main():
    # await cfg.db.async_session.drop_all_tables()
    await cfg.db.async_session.create_all_tables()

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

    await Book.delete_all()


if __name__ == '__main__':
    asyncio.run(async_main())
