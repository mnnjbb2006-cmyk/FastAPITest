## Purpose
Concise repo-specific guidance to help an AI agent make safe, correct edits quickly.

## Big picture
- Single-file FastAPI service in `main.py`. The ASGI app variable is named `api` (not `app`).
- Data is in-memory: `books` is a mutable list of Pydantic `Book` instances. No DB or external services.
- Responses currently keep a top-level object: `{ "books": [...] }` for the search endpoint.

## Public routes of interest
- GET `/` — query param `q: Annotated[str, Field(min_length=3)]`; returns `{ "books": [...] }`.
- PUT `/update/{book_id}` — updates a book by stable `book_id` and returns the updated `Book`.
- POST `/add/` — accepts `BookBase`, returns created `Book`.
- DELETE `/delete/{book_id}` — removes book by `book_id`.

## Conventions & constraints
- Attach new routes to `api` (e.g. `@api.get(...)`).
- Prefer `response_model` and Pydantic models for clear OpenAPI, but preserve `{ "books": [...] }` for backward compatibility unless README/docs are updated.
- `book_id` is the stable identifier; do not use Python list index as the id.
- Use `Annotated` + `Field` for request validation (preserve existing min/max constraints).
- Data is ephemeral (in-memory). Expect changes to be lost on restart.

## How to run (project-specific)
- Create venv & activate:
  - python -m venv .venv && source .venv/bin/activate
- Install deps:
  - pip install -r requirements.txt
- Dev server (recommended):
  - fastapi dev main.py  (OpenAPI at /docs)
- Alternative:
  - uvicorn main:api --reload --port 8000  (note `main:api`)

## Editing hints
- When changing response shapes, update README.md and call out breaking changes.
- To safely update a book by id: iterate `books`, match `b.book_id == book_id`, apply non-None fields from `BookUpdate`, return the modified `Book`.
- Example small additions:
  - Publishers list: `@api.get('/publishers', response_model=List[str])` return a deduplicated list from `books`.
- Keep endpoints synchronous (`def`) unless adding async work deliberately.

## What is NOT present
- No tests, CI, Dockerfile, or structured logging. Consider adding tests/CI as separate changes.
