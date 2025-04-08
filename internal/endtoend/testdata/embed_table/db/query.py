# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.28.0
# source: query.sql
import dataclasses
import datetime
from typing import AsyncIterator, Iterator, Optional

import sqlalchemy
import sqlalchemy.ext.asyncio

from db import models


CREATE_AUTHOR = """-- name: create_author \\:one
INSERT INTO authors (
  name, bio
) VALUES (
  :p1, :p2
)
RETURNING id, name, bio
"""


CREATE_BOOK = """-- name: create_book \\:one
INSERT INTO books (
  title, author_id, isbn, published
) VALUES (
  :p1, :p2, :p3, :p4
)
RETURNING id, title, author_id, isbn, published
"""


GET_BOOK_WITH_AUTHOR = """-- name: get_book_with_author \\:one
SELECT 
  b.id, b.title, b.author_id, b.isbn, b.published,
  a.author, a.author, a.author AS author
FROM books b
JOIN authors a ON b.author_id = a.id
WHERE b.id = :p1 LIMIT 1
"""


@dataclasses.dataclass()
class GetBookWithAuthorRow:
    id: int
    title: str
    author_id: int
    isbn: str
    published: datetime.date
    authors: models.Author


LIST_BOOKS_WITH_AUTHORS = """-- name: list_books_with_authors \\:many
SELECT 
  b.id, b.title, b.author_id, b.isbn, b.published,
  a.author, a.author, a.author AS author
FROM books b
JOIN authors a ON b.author_id = a.id
ORDER BY b.title
"""


@dataclasses.dataclass()
class ListBooksWithAuthorsRow:
    id: int
    title: str
    author_id: int
    isbn: str
    published: datetime.date
    authors: models.Author


class Querier:
    def __init__(self, conn: sqlalchemy.engine.Connection):
        self._conn = conn

    def create_author(self, *, name: str, bio: Optional[str]) -> Optional[models.Author]:
        row = self._conn.execute(sqlalchemy.text(CREATE_AUTHOR), {"p1": name, "p2": bio}).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            bio=row[2],
        )

    def create_book(self, *, title: str, author_id: int, isbn: str, published: datetime.date) -> Optional[models.Book]:
        row = self._conn.execute(sqlalchemy.text(CREATE_BOOK), {
            "p1": title,
            "p2": author_id,
            "p3": isbn,
            "p4": published,
        }).first()
        if row is None:
            return None
        return models.Book(
            id=row[0],
            title=row[1],
            author_id=row[2],
            isbn=row[3],
            published=row[4],
        )

    def get_book_with_author(self, *, id: int) -> Optional[GetBookWithAuthorRow]:
        row = self._conn.execute(sqlalchemy.text(GET_BOOK_WITH_AUTHOR), {"p1": id}).first()
        if row is None:
            return None
        return GetBookWithAuthorRow(
            id=row[0],
            title=row[1],
            author_id=row[2],
            isbn=row[3],
            published=row[4],
            authors=models.Author(
                id=row[5],
                name=row[6],
                bio=row[7],
            ),
        )

    def list_books_with_authors(self) -> Iterator[ListBooksWithAuthorsRow]:
        result = self._conn.execute(sqlalchemy.text(LIST_BOOKS_WITH_AUTHORS))
        for row in result:
            yield ListBooksWithAuthorsRow(
                id=row[0],
                title=row[1],
                author_id=row[2],
                isbn=row[3],
                published=row[4],
                authors=models.Author(
                    id=row[5],
                    name=row[6],
                    bio=row[7],
                ),
            )


class AsyncQuerier:
    def __init__(self, conn: sqlalchemy.ext.asyncio.AsyncConnection):
        self._conn = conn

    async def create_author(self, *, name: str, bio: Optional[str]) -> Optional[models.Author]:
        row = (await self._conn.execute(sqlalchemy.text(CREATE_AUTHOR), {"p1": name, "p2": bio})).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            bio=row[2],
        )

    async def create_book(self, *, title: str, author_id: int, isbn: str, published: datetime.date) -> Optional[models.Book]:
        row = (await self._conn.execute(sqlalchemy.text(CREATE_BOOK), {
            "p1": title,
            "p2": author_id,
            "p3": isbn,
            "p4": published,
        })).first()
        if row is None:
            return None
        return models.Book(
            id=row[0],
            title=row[1],
            author_id=row[2],
            isbn=row[3],
            published=row[4],
        )

    async def get_book_with_author(self, *, id: int) -> Optional[GetBookWithAuthorRow]:
        row = (await self._conn.execute(sqlalchemy.text(GET_BOOK_WITH_AUTHOR), {"p1": id})).first()
        if row is None:
            return None
        return GetBookWithAuthorRow(
            id=row[0],
            title=row[1],
            author_id=row[2],
            isbn=row[3],
            published=row[4],
            authors=models.Author(
                id=row[5],
                name=row[6],
                bio=row[7],
            ),
        )

    async def list_books_with_authors(self) -> AsyncIterator[ListBooksWithAuthorsRow]:
        result = await self._conn.stream(sqlalchemy.text(LIST_BOOKS_WITH_AUTHORS))
        async for row in result:
            yield ListBooksWithAuthorsRow(
                id=row[0],
                title=row[1],
                author_id=row[2],
                isbn=row[3],
                published=row[4],
                authors=models.Author(
                    id=row[5],
                    name=row[6],
                    bio=row[7],
                ),
            )
