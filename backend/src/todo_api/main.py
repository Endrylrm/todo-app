from fastapi import FastAPI

from .databases.sqlite import SQLiteDB
from .repositories.todo_sqlite_repository import TodoSQLiteRepository
from .services.todo_service import TodoService
from .controllers.todo_controller import TodoController

app = FastAPI()
db = SQLiteDB("database/todo.db")
db.init_db()

repository = TodoSQLiteRepository(db.create_connection())
service = TodoService(repository)
controller = TodoController(service)

app.include_router(controller.router)


@app.get("/")
@app.get("/api")
async def root():
    return {"message": "Welcome to todo api!"}
