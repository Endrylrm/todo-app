from fastapi import FastAPI

app = FastAPI()


@app.get("/")
@app.get("/api")
async def root():
    return {"message": "Welcome to todo api!"}


@app.get("/api/todos")
async def get_todos():
    return {}


@app.get("/api/todos/{id}")
async def get_todo(id: int):
    return {}


@app.patch("/api/todos/{id}")
async def update_todo(id: int, todo: dict):
    return {}


@app.put("/api/todos/{id}")
async def update_todo_completely(id: int, todo: dict):
    return {}


@app.delete("/api/todos/{id}")
async def delete_todo(id: int):
    return {}
