from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .databases.sqlite import SQLiteDB
from .repositories.todo_sqlite_repository import TodoSQLiteRepository
from .services.todo_service import TodoService
from .controllers.todo_controller import TodoController

from .exceptions.errors import (
    TodoNotFoundError,
    TodoInvalidDataError,
    TodoEmptyDataError,
)

app = FastAPI()
db = SQLiteDB("database/todo.db")
db.init_db()

repository = TodoSQLiteRepository(db.create_connection())
service = TodoService(repository)
controller = TodoController(service)


@app.exception_handler(TodoNotFoundError)
async def todo_not_found_handler(request: Request, exc: TodoNotFoundError):
    return JSONResponse(status_code=404, content={"error": f"Todo {exc.id} not found!"})


@app.exception_handler(TodoInvalidDataError)
async def todo_invalid_data_handler(request: Request, exc: TodoInvalidDataError):
    return JSONResponse(
        status_code=422, content={"error": f"No '{exc.variable}' in request!"}
    )


@app.exception_handler(TodoEmptyDataError)
async def todo_empty_data_handler(request: Request, exc: TodoEmptyDataError):
    return JSONResponse(status_code=400, content={"error": f"{exc.message}"})


app.include_router(controller.router)


@app.get("/")
@app.get("/api")
async def root():
    return {"message": "Welcome to todo api!"}
