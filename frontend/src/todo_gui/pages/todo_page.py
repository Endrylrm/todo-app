from nicegui import ui

from models.todo import Todo
from components.todo_card import TodoCard
from services.api_client_service import APIClientService


class TodoPage:
    def __init__(self, api_client: APIClientService):
        self._api_client = api_client
        self.todos = self._api_client.get_todos()

        self.render()

    def render(self):
        with ui.row():
            with ui.link(target="/add"):
                ui.button("Add Task", icon="add", color="green")
        with ui.grid(columns=4).classes("w-full gap-4"):
            if not self.todos:
                ui.label(
                    "No task yet, please click on 'Add Task' to add a new one"
                ).classes("text-4xl col-span-4")
            for todo in self.todos:
                TodoCard(todo, self._api_client)
