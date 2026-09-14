from fastapi import FastAPI

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
