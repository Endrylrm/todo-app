import sqlite3

from fastapi import FastAPI

from .repositories.todo_sqlite_repository import TodoSQLiteRepository
from .services.todo_service import TodoService
from .controllers.todo_controller import TodoController


def create_sqlite_connection(self) -> sqlite3.Connection:
    conn = sqlite3.connect(self._path)
    return conn


app = FastAPI()

repository = TodoSQLiteRepository(create_sqlite_connection("database/todo.db"))
service = TodoService(repository)
controller = TodoController(service)

app.include_router(controller.router)


@app.get("/")
@app.get("/api")
async def root():
    return {"message": "Welcome to todo api!"}
