-- name: GetBookWithAuthor :one
SELECT 
  b.*,
  sqlc.embed(a) AS author
FROM books b
JOIN authors a ON b.author_id = a.id
WHERE b.id = $1 LIMIT 1;

-- name: ListBooksWithAuthors :many
SELECT 
  b.*,
  sqlc.embed(a) AS author
FROM books b
JOIN authors a ON b.author_id = a.id
ORDER BY b.title;

-- name: CreateAuthor :one
INSERT INTO authors (
  name, bio
) VALUES (
  $1, $2
)
RETURNING *;

-- name: CreateBook :one
INSERT INTO books (
  title, author_id, isbn, published
) VALUES (
  $1, $2, $3, $4
)
RETURNING *;
