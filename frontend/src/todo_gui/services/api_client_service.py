import requests

from models.todo import Todo

from exceptions.errors import APIError


class APIClientService:
    def __init__(self, url: str):
        self._url = url

    def get_todos(self) -> list[Todo]:
        request = self._request("GET")

        todos = []
        for todo in request["data"]:
            todos.append(Todo.from_api(todo))

        return todos

    def get_todo(self, id: int) -> Todo:
        request = self._request("GET", f"/{id}")

        todo = Todo.from_api(request["data"])
        return todo

    def insert_todo(self, todo: Todo) -> Todo:
        payload = {
            "title": todo.title,
            "description": todo.description,
            "is_active": todo.is_active,
        }
        request = self._request("POST", json=payload)
        todo = Todo.from_api(request["data"])
        return todo

    def update_todo(self, todo: Todo) -> Todo:
        payload = {
            "title": todo.title,
            "description": todo.description,
            "is_active": todo.is_active,
        }
        request = self._request("PUT", f"/{todo.id}", json=payload)
        todo = Todo.from_api(request["data"])
        return todo

    def delete_todo(self, id: int):
        self._request("DELETE", f"/{id}")

    def _request(self, method: str, path: str = "", **kwargs):
        response = requests.request(method, self._url + path, **kwargs)

        if not response.ok:
            msg = response.json().get("error", "unexpected error!")
            raise APIError(response.status_code, msg)

        if response.status_code == 204:
            return None

        return response.json()
