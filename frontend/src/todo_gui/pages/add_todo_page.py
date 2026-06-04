from nicegui import ui

from models.todo import Todo

from services.api_client_service import APIClientService


class AddTodoPage:
    def __init__(self, api_client: APIClientService):
        self._api_client = api_client

        self.render()

    def render(self):
        with ui.grid(columns=1).classes("w-full gap-1"):
            title = ui.input("Title:")
            description = ui.input("Description:")
            is_active = ui.checkbox("Is Active?", value=True)
            with ui.row():
                ui.button(
                    "Add new Task",
                    icon="add",
                    on_click=lambda: self._create_todo(
                        title.value, description.value, is_active.value
                    ),
                    color="green",
                )
                with ui.link(target="/"):
                    ui.button("Return Home", icon="home")

    def _create_todo(self, title: str, description: str, is_active: bool):
        self._api_client.insert_todo(Todo(None, title, description, is_active))
        ui.notify(f"Task Created!")
