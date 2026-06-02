from nicegui import ui

from models.todo import Todo
from components.todo_card import TodoCard
from services.api_service import APIService


class TodoPage:
    def __init__(self, service: APIService):
        self._service = service

        self.render()

    def render(self):
        todos = self._service.get_todos()
        with ui.row():
            with ui.link(target="/add"):
                ui.button("Add Todo", icon="add", color="green")
        with ui.grid(columns=4).classes("w-full gap-4"):
            for todo in todos:
                TodoCard(int(todo), todos[todo], self._service)
