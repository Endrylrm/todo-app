import sqlite3

from typing import Any

from fastapi import FastAPI, status

from .models.todo import Todo

app = FastAPI()

conn = sqlite3.connect("database/todo.db")


def create_table():
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            is_active BOOLEAN
        )
    """)


create_table()


@app.get("/")
@app.get("/api")
async def root():
    return {"message": "Welcome to todo api!"}


@app.get("/api/todos", status_code=status.HTTP_200_OK)
async def get_todos() -> dict[str, Todo]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos")
    todos_rows = cursor.fetchall()
    todos = {}

    for todo in todos_rows:
        todos[str(todo[0])] = Todo(
            title=todo[1], description=todo[2], is_active=todo[3]
        )
    return todos


@app.get("/api/todos/{id}", status_code=status.HTTP_200_OK)
async def get_todo(id: int) -> dict[str, Todo]:
    if id < 1:
        return {"failed": "Invalid id range!"}

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos WHERE id = ?", (id,))
    todo_row = cursor.fetchone()
    todo: dict[str, Todo] = {
        str(todo_row[0]): Todo(
            title=todo_row[1], description=todo_row[2], is_active=todo_row[3]
        )
    }
    return todo


@app.post("/api/todos", status_code=status.HTTP_201_CREATED)
async def insert_todo(todo: Todo) -> dict[str, Any]:
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO todos (title, description, is_active) VALUES (?, ?, ?)",
            (
                todo.title,
                todo.description,
                int(todo.is_active),
            ),
        )
        conn.commit()
        return {"success": "todo created!"}

    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
        return {"failed": "unable to create todo!", "error": e}


@app.patch("/api/todos/{id}", status_code=status.HTTP_200_OK)
async def update_todo(id: int, todo: Todo) -> dict[str, Any]:
    if id < 1:
        return {"failed": "Invalid id range!"}

    try:
        cursor = conn.cursor()
        sql = "UPDATE todos SET "
        temp_parameter_list = []

        if todo.title is not None:
            sql = sql + "title = ?,"
            temp_parameter_list.append(todo.title)

        if todo.description is not None:
            sql = sql + "description = ?,"
            temp_parameter_list.append(todo.description)

        if todo.is_active is not None:
            sql = sql + "is_active = ?,"
            temp_parameter_list.append(int(todo.is_active))

        sql = sql.rstrip(",") + " WHERE id = ?"

        temp_parameter_list.append(id)

        cursor.execute(
            sql,
            tuple(temp_parameter_list),
        )
        conn.commit()
        return {"success": "todo updated!"}

    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
        return {"failed": "unable to update todo!", "error": e}


@app.put("/api/todos/{id}", status_code=status.HTTP_200_OK)
async def update_todo_completely(id: int, todo: Todo) -> dict[str, Any]:
    if id < 1:
        return {"failed": "Invalid id range!"}

    if todo.title is None:
        return {"failed": "No 'title' to update todo completely!"}

    if todo.description is None:
        return {"failed": "No 'description' to update todo completely!"}

    if todo.is_active is None:
        return {"failed": "No 'is_active' to update todo completely"}

    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE todos SET title = ?, description = ?, is_active = ? WHERE id = ?",
            (todo.title, todo.description, int(todo.is_active), id),
        )
        conn.commit()
        return {"success": "todo updated completely!"}

    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
        return {"failed": "unable to update todo completely!", "error": e}


@app.delete("/api/todos/{id}", status_code=status.HTTP_200_OK)
async def delete_todo(id: int) -> dict[str, Any]:
    if id < 1:
        return {"failed": "Invalid id range!"}

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ?", (id,))
        conn.commit()
        return {"success": "todo deleted!"}

    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
        return {"failed": "unable to delete todo!", "error": e}
