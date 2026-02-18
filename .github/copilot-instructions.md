## Purpose

Short instructions to help an AI agent become productive in this repository quickly.

## Big picture

- Single-file FastAPI service in `main.py`. The ASGI app is named `api` (not `app`).
- Data is in-memory: `books` is a list of Pydantic `Book` instances (no DB, no background workers).
- Current public routes of interest:
  - GET `/` — query param `q` (Annotated, min_length=3); returns List[Book] (response_model).
  - PUT `/update/{book_id}` — updates a book by its `book_id` and returns the updated `Book`.

## Key files

- `main.py` — FastAPI app, Pydantic models (`Book`, `BookUpdate`), and the in-memory `books` list.
- `README.md` — quick-start and the recommended dev run command.
- `requirements.txt` — dependency manifest (uses `fastapi` and `fastapi[standard]`).

## How to run (project-specific)

Follow `README.md`. Short checklist:
- Create/activate venv: `python -m venv .venv && source .venv/bin/activate`
- Install deps: `pip install -r requirements.txt`
- Dev server (recommended): `fastapi dev main.py` (OpenAPI at `/docs`)
- Alternative: `uvicorn main:api --reload --port 8000` (note `main:api`).

## Project-specific conventions

- Attach new endpoints to `api` (e.g. `@api.get(...)`).
- Prefer using the existing Pydantic models and `response_model` for endpoints. `Book` and `BookUpdate` are defined in `main.py`.
- `book_id` is the stable identifier used by the update endpoint; do not treat Python list index as the id.
- Request validation uses `Annotated` + `Field` constraints (e.g. `q` min_length and `year` range). Preserve these constraints when adding params.
- Data is mutable in-memory: changes are ephemeral and lost on restart — useful for local testing only.

## Editing hints with examples

- Add a simple publishers endpoint:
  - `@api.get('/publishers', response_model=List[str])` and return a deduplicated list from `books`.
- When adding/updating routes that change response shapes, update `README.md` or mention breaking changes in the PR.
- Example: safely update a book by id (pattern used in `main.py`): iterate `books`, match `b.book_id == book_id`, apply non-None fields from `BookUpdate` and return the `Book`.

## What is NOT present

- No tests, no CI, no Dockerfile, no structured logging/tracing. Expect manual local development.

## Where to look for more context

- `main.py` — canonical source for API behavior and data.
- `README.md` — run instructions and example query usage.

If you'd like I can expand this with: a tiny pytest harness for the endpoints, a sample `docker-compose` or a minimal CI workflow. Tell me which and I'll add it.
## Purpose

Short instructions to help an AI agent become productive in this repository quickly.

## Big picture

- This is a very small FastAPI service implemented entirely in `main.py`.
- The app instance is named `api` (not the common `app`). New endpoints should attach to `api`.
- Data is in-memory: `books` is a list of plain Python dicts defined in `main.py`. There is no database, background workers, or external services.
- A Pydantic model `Book` is defined but the current endpoint returns raw dicts inside a top-level dict `{"books": [...]}`.

## Key files

- `main.py` — single source of truth: FastAPI app, `Book` model, `books` data, and the `find_books` GET `/` endpoint.
- `README.md` — quick-start and the project-recommended run command.
- `requirements.txt` — lists `fastapi` and `fastapi[standard]` and is the authoritative dependency list.

## How to run (project-specific)

Follow the steps in `README.md`:
- Create and activate a virtualenv (project uses `.venv` in example).
- Install deps: `pip install -r requirements.txt`.
- Start dev server (as the README shows): `fastapi dev main.py` — this runs the app and exposes OpenAPI at `/docs`.

Note: the app variable name is `api`, so when referencing the ASGI application in tools or tests use `main:api`.

## Patterns and conventions an AI should follow

- Keep the top-level response shape `{ "books": [...] }` for backward compatibility when editing `find_books`.
- Follow the existing synchronous endpoint style (plain `def`, returning Python dicts) unless adding async work explicitly.
- Use the `Book` Pydantic model for request/response schemas when adding new endpoints, but be aware current responses use raw dicts—if you switch to returning `Book` (or `List[Book]`) update examples/docs accordingly.
- Query parameter usage: `find_books(q: str)` expects a `q` query parameter. The README demonstrates usage `/?q=math` — keep this contract or update README if changing it.

## Integration and external dependencies

- No external integrations in the codebase. All runtime behavior is local and driven by `main.py` and FastAPI.
- Dependencies are declared in `requirements.txt`. There is no CI configuration or test runner present in the repository.

## Editing hints (practical examples)

- To add an endpoint that lists publishers, edit `main.py` and attach a new route to `api`, e.g. `@api.get('/publishers')`.
- If you change the ASGI callable name, update `README.md` run instructions and any tooling that references `main:api`.
- When returning structured responses, prefer returning Pydantic models for clear OpenAPI output, but maintain the existing top-level `books` key if you want to preserve the current front-end expectations.

## Things NOT present / what to expect

- There are no tests, no Dockerfile, and no CI configuration in the repository.
- No logging or structured tracing is configured.

## Where to look for more context

- `main.py` — everything you need to change or extend the service.
- `README.md` — run instructions and examples used by humans; keep it in sync with code changes.

If anything here is unclear or you'd like the file to include extra rules (style, tests, CI), tell me which topics to expand and I'll iterate.
