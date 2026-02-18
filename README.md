# FastApiTest

A tiny FastAPI example that serves a small in-memory list of books and provides a simple search endpoint.

Features
- GET /?q=search_term — returns books whose title or author contains the search term (case-insensitive).
- OpenAPI docs available at /docs when the server is running.

Quick start

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app with fastapi:

```bash
fastapi dev main.py
```

4. Open your browser:
- API root: http://127.0.0.1:8000/?q=weapon
- Swagger UI: http://127.0.0.1:8000/docs

Notes
- The search endpoint returns a top-level JSON object with the `books` key, e.g.:

```json
{
	"books": [
		{
			"book_id": 1,
			"title": "Weapons of Math Destruction",
			"author": "Cathy O'Neil",
			"year": 2016,
			"publisher": "Penguin Books, Limited"
		}
	]
}
```

Validation
- The `q` query parameter requires at least 3 characters. Other models use `Annotated` + `Field` constraints — invalid requests return a 422 with details.

Endpoints
- GET /?q=search_term — search books by title or author (case-insensitive). Returns `{ "books": [...] }`.
- POST /add/ — add a book (request body uses `BookBase`). Returns the created `Book`.
- PUT /update/{book_id} — update a book by `book_id` (partial fields allowed via `BookUpdate`). Returns the updated `Book`.
- DELETE /delete/{book_id} — delete a book by `book_id`.
