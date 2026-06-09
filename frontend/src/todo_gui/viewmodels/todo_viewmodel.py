from nicegui import ui

from events.todo import todo_created, todo_updated, todo_deleted

from models.todo import Todo

from services.api_client_service import APIClientService


class TodoViewmodel:
    def __init__(self, api_client: APIClientService):
        self._api_client = api_client
        self.todos: list[Todo] = []

        self.get_todos()

    def get_todos(self) -> list[Todo]:
        self.todos = self._api_client.get_todos()

    def get_todo(self, id: int) -> Todo:
        todo = self._api_client.get_todo(id)
        return todo

    def insert_todo(self, todo: Todo):
        new_todo = self._api_client.insert_todo(todo)

        if not todo:
            ui.notify("Unable to add task!", type="negative")
            return

        self.todos.append(new_todo)
        todo_created.emit()
        ui.notify(f"Task Created!", type="positive")

    def update_todo(self, todo: Todo):
        updated_todo = self._api_client.update_todo(todo)

        if not updated_todo:
            ui.notify("Unable to update task!", type="negative")
            return

        for task in self.todos:
            if task.id == todo.id:
                task.title = updated_todo.title
                task.description = updated_todo.description
                task.is_active = updated_todo.is_active
                task.updated_at = updated_todo.updated_at
        todo_updated.emit()
        ui.notify(f"Task with id: {id} Updated!", type="warning")

    def delete_todo(self, id: int):
        todo_to_remove = next(filter(lambda todo: todo.id == id, self.todos))
        self._api_client.delete_todo(id)
        self.todos.remove(todo_to_remove)
        todo_deleted.emit()
        ui.notify(f"Task with id: {id} Deleted!", type="negative")
