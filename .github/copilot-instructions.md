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
