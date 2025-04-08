CREATE TABLE authors (
  id   BIGSERIAL PRIMARY KEY,
  name TEXT      NOT NULL,
  bio  TEXT
);

CREATE TABLE books (
  id        BIGSERIAL PRIMARY KEY,
  title     TEXT      NOT NULL,
  author_id BIGINT    NOT NULL REFERENCES authors(id),
  isbn      TEXT      NOT NULL,
  published DATE      NOT NULL
);
