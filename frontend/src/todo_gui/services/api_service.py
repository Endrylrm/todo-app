import requests

from models.todo import Todo


class APIService:
    def __init__(self, url: str):
        self._url = url

    def get_todos(self) -> dict[str, Todo]:
        r = requests.get(self._url)

        todos = {}
        for key in r.json():
            todos[key] = Todo(**r.json()[key])

        return todos

    def get_todo(self, id: int) -> dict[str, Todo]:
        r = requests.get(f"{self._url}/{id}")

        for key in r.json():
            todo = Todo(**r.json()[key])

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
