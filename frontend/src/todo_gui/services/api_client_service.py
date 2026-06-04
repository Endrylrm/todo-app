import requests

from models.todo import Todo

from exceptions.errors import APIError


class APIClientService:
    def __init__(self, url: str):
        self._url = url

    def get_todos(self) -> dict[str, Todo]:
        r = self._request("GET")

        todos = {}
        for todo in r["todos"]:
            id = todo["id"]
            todo_params = {key: value for key, value in todo.items() if key != "id"}
            todos[str(id)] = Todo(**todo_params)

        return todos

    def get_todo(self, id: int) -> Todo:
        r = self._request("GET", f"/{id}")

        todo_params = {key: value for key, value in r.items() if key != "id"}
        todo = Todo(**todo_params)
        return todo

    def insert_todo(self, todo: Todo):
        payload = {
            "title": todo.title,
            "description": todo.description,
            "is_active": todo.is_active,
        }
        self._request("POST", f"/{id}", json=payload)

    def update_todo(self, id: int, todo: Todo):
        payload = {
            "title": todo.title,
            "description": todo.description,
            "is_active": todo.is_active,
        }
        self._request("PUT", f"/{id}", json=payload)

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
