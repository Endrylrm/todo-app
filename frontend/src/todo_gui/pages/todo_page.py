from nicegui import ui

from models.todo import Todo
from components.todo_card import TodoCard
from services.api_client_service import APIClientService


class TodoPage:
    def __init__(self, api_client: APIClientService):
        self._api_client = api_client

        self.render()

    def render(self):
        todos = self._api_client.get_todos()
        with ui.row():
            with ui.link(target="/add"):
                ui.button("Add Todo", icon="add", color="green")
        with ui.grid(columns=4).classes("w-full gap-4"):
            if not todos:
                with ui.grid(columns=1).classes("w-full gap-4 place-items-center"):
                    ui.label(
                        "No todos yet, please click on 'Add Todo' to add a new one"
                    ).classes("text-5xl")
            for todo in todos:
                TodoCard(todo, self._api_client)
