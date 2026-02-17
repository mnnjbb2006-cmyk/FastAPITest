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
- API root: http://127.0.0.1:8000/?q=math
- Swagger UI: http://127.0.0.1:8000/docs
