from models.todo import Todo

from services.api_client_service import APIClientService


class TodoViewmodel:
    def __init__(self, api_client: APIClientService):
        self._api_client = api_client
        self.todos: list[Todo] = []

    def get_todos(self) -> list[Todo]:
        self.todos = self._api_client.get_todos()

    def get_todo(self, id: int) -> Todo:
        todo = self._api_client.get_todo(id)
        return todo

    def insert_todo(self, todo: Todo):
        self._api_client.insert_todo(todo)

    def update_todo(self, todo: Todo):
        self._api_client.update_todo(todo)
        for task in self.todos:
            if task.id == todo.id:
                task.title = todo.title
                task.description = todo.description
                task.is_active = todo.is_active

    def delete_todo(self, id: int):
        todo_to_remove = next(filter(lambda todo: todo.id == id, self.todos))
        self._api_client.delete_todo(id)
        self.todos.remove(todo_to_remove)
