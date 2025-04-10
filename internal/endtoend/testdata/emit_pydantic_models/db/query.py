# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.28.0
# source: query.sql
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


DELETE_AUTHOR = """-- name: delete_author \\:exec
DELETE FROM authors
WHERE id = :p1
"""


GET_AUTHOR = """-- name: get_author \\:one
SELECT id, name, bio FROM authors
WHERE id = :p1 LIMIT 1
"""


LIST_AUTHORS = """-- name: list_authors \\:many
SELECT id, name, bio FROM authors
ORDER BY name
"""


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

    def delete_author(self, *, id: int) -> None:
        self._conn.execute(sqlalchemy.text(DELETE_AUTHOR), {"p1": id})

    def get_author(self, *, id: int) -> Optional[models.Author]:
        row = self._conn.execute(sqlalchemy.text(GET_AUTHOR), {"p1": id}).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            bio=row[2],
        )

    def list_authors(self) -> Iterator[models.Author]:
        result = self._conn.execute(sqlalchemy.text(LIST_AUTHORS))
        for row in result:
            yield models.Author(
                id=row[0],
                name=row[1],
                bio=row[2],
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

    async def delete_author(self, *, id: int) -> None:
        await self._conn.execute(sqlalchemy.text(DELETE_AUTHOR), {"p1": id})

    async def get_author(self, *, id: int) -> Optional[models.Author]:
        row = (await self._conn.execute(sqlalchemy.text(GET_AUTHOR), {"p1": id})).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            bio=row[2],
        )

    async def list_authors(self) -> AsyncIterator[models.Author]:
        result = await self._conn.stream(sqlalchemy.text(LIST_AUTHORS))
        async for row in result:
            yield models.Author(
                id=row[0],
                name=row[1],
                bio=row[2],
            )
