import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .databases.sqlite_db import SQLiteDB
from .repositories.todo_sqlite_repository import TodoSQLiteRepository
from .services.todo_service import TodoService
from .controllers.todo_controller import TodoController

from .exceptions.errors import (
    TodoNotFoundError,
    TodoInvalidDataError,
    TodoEmptyDataError,
    TodoNotCreatedError,
)

DB_URL = os.getenv("DATABASE_URL")
DB_TYPE = os.getenv("DATABASE_TYPE")

app = FastAPI()
db = None
repository = None

if DB_TYPE == "sqlite":
    db = SQLiteDB(DB_URL)
    repository = TodoSQLiteRepository(db.create_connection())
else:
    print("Unable to load the Database, check the Database Type!")

db.init_db()

service = TodoService(repository)
controller = TodoController(service)


@app.exception_handler(TodoNotFoundError)
async def todo_not_found_handler(request: Request, exc: TodoNotFoundError):
    return JSONResponse(
        status_code=404, content={"error": f"Todo with id: {exc.id} not found!"}
    )


@app.exception_handler(TodoInvalidDataError)
async def todo_invalid_data_handler(request: Request, exc: TodoInvalidDataError):
    return JSONResponse(
        status_code=422, content={"error": f"No '{exc.variable}' in request!"}
    )


@app.exception_handler(TodoEmptyDataError)
async def todo_empty_data_handler(request: Request, exc: TodoEmptyDataError):
    return JSONResponse(status_code=400, content={"error": f"{exc.message}"})


@app.exception_handler(TodoNotCreatedError)
async def todo_not_created_handler(request: Request, exc: TodoNotCreatedError):
    return JSONResponse(status_code=422, content={"error": f"{exc.message}"})


app.include_router(controller.router)


@app.get("/")
@app.get("/api")
async def root():
    return {"message": "Welcome to todo api!"}
