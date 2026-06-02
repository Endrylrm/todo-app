from fastapi import FastAPI

from .repositories.todo_repository import TodoRepository
from .services.todo_service import TodoService
from .controllers.todo_controller import TodoController

app = FastAPI()

repository = TodoRepository("database/todo.db")
service = TodoService(repository)
controller = TodoController(service)

app.include_router(controller.router)


@app.get("/")
@app.get("/api")
async def root():
    return {"message": "Welcome to todo api!"}
