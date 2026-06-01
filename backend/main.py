import sqlite3

from fastapi import FastAPI, status

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
async def get_todos():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos")
    todos_rows = cursor.fetchall()
    todos = {}

    for todo in todos_rows:
        todos[str(todo[0])] = {
            "title": todo[1],
            "description": todo[2],
            "is_active": bool(todo[3]),
        }
    return todos


@app.get("/api/todos/{id}", status_code=status.HTTP_200_OK)
async def get_todo(id: int):
    if id < 1:
        return {"failed": "Invalid id range!"}

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos WHERE id = ?", (id,))
    todo_row = cursor.fetchone()
    todo = {
        str(todo_row[0]): {
            "title": todo_row[1],
            "description": todo_row[2],
            "is_active": bool(todo_row[3]),
        }
    }
    return todo


@app.post("/api/todos", status_code=status.HTTP_201_CREATED)
async def insert_todo(todo: dict):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO todos (title, description, is_active) VALUES (?, ?, ?)",
            (
                todo["title"],
                todo["description"],
                int(todo["is_active"]),
            ),
        )
        conn.commit()
        return {"success": "todo created!"}

    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
        return {"failed": "unable to create todo!", "error": e}


@app.patch("/api/todos/{id}")
async def update_todo(id: int, todo: dict):
    return {}


@app.put("/api/todos/{id}")
async def update_todo_completely(id: int, todo: dict):
    return {}


@app.delete("/api/todos/{id}")
async def delete_todo(id: int):
    return {}
