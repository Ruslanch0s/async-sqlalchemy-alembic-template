import asyncio

from db.database import async_db_session
from db.models.book import Book


async def async_main():
    # await async_db_session.drop_all_tables()

    await async_db_session.create_all_tables()
    # await Book.create_book(name='qwe')
    book = Book(name='new')
    await book.create_me()

    b1 = Book(name='b1')
    b2 = Book(name='b2')
    b3 = Book(name='b3')
    await Book.create_some([b1, b2, b3])


if __name__ == '__main__':
    asyncio.run(async_main())
