from nicegui import ui

from models.todo import Todo
from components.todo_card import TodoCard
from services.api_service import APIService


class TodoPage:
    def __init__(self, service: APIService):
        self._service = service

        self.render()

    def render(self):
        with ui.row():
            with ui.link(target="/add"):
                ui.button("Add Todo", icon="add")
        with ui.grid(columns=4).classes("w-full gap-4"):
            for todo in self._service.todos:
                TodoCard(int(todo), self._service.todos[todo], self._service)
