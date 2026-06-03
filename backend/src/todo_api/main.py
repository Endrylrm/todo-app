import sqlite3

from fastapi import FastAPI

from .repositories.todo_sqlite_repository import TodoSQLiteRepository
from .services.todo_service import TodoService
from .controllers.todo_controller import TodoController


def create_sqlite_connection(path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    return conn


conn = create_sqlite_connection("database/todo.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        is_active BOOLEAN
    )
""")

app = FastAPI()

repository = TodoSQLiteRepository(conn)
service = TodoService(repository)
controller = TodoController(service)

app.include_router(controller.router)


@app.get("/")
@app.get("/api")
async def root():
    return {"message": "Welcome to todo api!"}
