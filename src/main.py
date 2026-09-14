from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

SEED_BOOKS = [
    {"id": 1, "title": "The Silent Planet", "author": "Mira Cole", "status": "unread"},
    {"id": 2, "title": "Beyond the River", "author": "Sam Rowan", "status": "reading"},
    {"id": 3, "title": "Glass Harbour", "author": "Elena Vale", "status": "finished"},
    {"id": 4, "title": "North of Tomorrow", "author": "Daniel Frost", "status": "unread"},
    {"id": 5, "title": "The Last Lantern", "author": "Nora Blake", "status": "reading"},
]

books = []
next_id = 1


def reset_state():
    """Internal test-support reset (rule 11). Not exposed as an HTTP route."""
    global books, next_id
    books = [dict(book) for book in SEED_BOOKS]
    next_id = 6


reset_state()


def _parse_pagination(page_raw, limit_raw):
    """Returns (page, limit) or None if invalid per rule 14."""
    try:
        page = int(page_raw)
        limit = int(limit_raw)
    except (TypeError, ValueError):
        return None
    if page < 1 or limit < 1 or limit > 50:
        return None
    return page, limit


@app.get("/books")
def list_books(page: str = "1", limit: str = "10"):
    # rules 12-16
    parsed = _parse_pagination(page, limit)
    if parsed is None:
        return JSONResponse(status_code=400, content={"error": "Invalid pagination"})
    page_num, limit_num = parsed
    ordered_books = sorted(books, key=lambda book: book["id"])
    start = (page_num - 1) * limit_num
    end = start + limit_num
    return ordered_books[start:end]


def _parse_book_id(book_id_raw):
    """Returns a positive int book id, or None if invalid per rule 17."""
    try:
        book_id = int(book_id_raw)
    except (TypeError, ValueError):
        return None
    if book_id < 1:
        return None
    return book_id


def _find_book(book_id):
    return next((book for book in books if book["id"] == book_id), None)


@app.get("/books/{book_id}")
def get_book(book_id: str):
    # rules 17-19
    parsed_id = _parse_book_id(book_id)
    if parsed_id is None:
        return JSONResponse(status_code=400, content={"error": "Invalid book id"})
    book = _find_book(parsed_id)
    if book is None:
        return JSONResponse(status_code=404, content={"error": "Book not found"})
    return book
