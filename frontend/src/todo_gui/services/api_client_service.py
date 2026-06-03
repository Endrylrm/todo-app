import requests

from models.todo import Todo


class APIClientService:
    def __init__(self, url: str):
        self._url = url

    def get_todos(self) -> dict[str, Todo]:
        r = requests.get(self._url)

        todos = {}
        for todo in r.json()["todos"]:
            id = todo["id"]
            todo_params = {key: value for key, value in todo.items() if key != "id"}
            todos[str(id)] = Todo(**todo_params)

        return todos

    def get_todo(self, id: int) -> Todo:
        r = requests.get(f"{self._url}/{id}")

        todo_params = {key: value for key, value in r.json().items() if key != "id"}
        todo = Todo(**todo_params)
        return todo

    def insert_todo(self, todo: Todo):
        payload = {
            "title": todo.title,
            "description": todo.description,
            "is_active": todo.is_active,
        }
        r = requests.post(self._url, json=payload)
        print(r.request.body.decode())

    def update_todo(self, id: int, todo: Todo):
        payload = {
            "title": todo.title,
            "description": todo.description,
            "is_active": todo.is_active,
        }
        r = requests.put(f"{self._url}/{id}", json=payload)

    def delete_todo(self, id: int):
        r = requests.delete(f"{self._url}/{id}")
