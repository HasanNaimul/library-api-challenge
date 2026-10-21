# Personal Library API

A specification-driven FastAPI exercise for managing an in-memory collection of books. It demonstrates request validation, predictable HTTP errors, pagination and acceptance testing against a written contract.

## Where is the implementation?

The default branch holds [SPEC.md](SPEC.md). The completed implementation and its tests are on the existing **`hasan-naimul-w2d1-challenge`** branch:

- [Browse the implementation](https://github.com/HasanNaimul/library-api-challenge/tree/hasan-naimul-w2d1-challenge)
- [Application source](https://github.com/HasanNaimul/library-api-challenge/blob/hasan-naimul-w2d1-challenge/src/main.py)
- [Acceptance tests](https://github.com/HasanNaimul/library-api-challenge/blob/hasan-naimul-w2d1-challenge/tests/test_api.py)

This introduction does not merge branches or change the default branch.

## Run the implementation

Clone the implementation branch directly:

```bash
git clone --branch hasan-naimul-w2d1-challenge https://github.com/HasanNaimul/library-api-challenge.git
cd library-api-challenge
python -m venv .venv
```

Activate `.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` on macOS/Linux. Then:

```bash
python -m pip install -r requirements.txt
python -m uvicorn src.main:app --reload --port 8000
```

Use `http://127.0.0.1:8000/docs` to explore the endpoints. The audit used Python 3.12; the repository does not pin dependency versions. No database, API keys or external services are required.

| Method | Path | Behaviour |
| --- | --- | --- |
| GET | `/books` | Paginated list; `page` defaults to 1 and `limit` to 10 |
| GET | `/books/{book_id}` | Retrieve a book |
| POST | `/books` | Create a book with title, author and status |
| PATCH | `/books/{book_id}` | Update status only |
| DELETE | `/books/{book_id}` | Delete a book; return 204 |

Valid statuses are `unread`, `reading` and `finished`. For example:

```bash
curl 'http://127.0.0.1:8000/books?page=1&limit=2'
```

For POST requests, use the interactive docs with:

```json
{"title": "Example book", "author": "Example author", "status": "unread"}
```

## Verification

On the implementation branch:

```bash
python -m pytest -q
```

All **91 existing acceptance tests passed** in the October 2026 review at implementation commit `87782a2`. One FastAPI/Starlette test-client dependency deprecation warning was emitted. Tests exercise success paths, boundary values, validation priorities, malformed bodies, missing records and state reset. This is a measured test result, not a claim of complete coverage.

## Scope and limitations

The service starts with five synthetic books and stores changes in process memory. Restarting the process resets the collection. There is no authentication, persistent database or multi-process consistency guarantee. It is a local learning application, not a production library service.

The existing specification, implementation, tests and history are preserved. The original implementation README retains its historical instructions; the commands above specify the actual repository and branch. Future work could include pinned dependencies and persistent storage, with explicit changes to the current contract.
