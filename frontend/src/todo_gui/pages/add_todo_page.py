from nicegui import ui

from models.todo import Todo

from services.api_service import APIService


class AddTodoPage:
    def __init__(self, service: APIService):
        self._service = service

        self.render()

    def render(self):
        with ui.grid(columns=1).classes("w-full gap-1"):
            title = ui.input("Title:")
            description = ui.input("Description:")
            is_active = ui.switch("Is Active")
            with ui.row():
                ui.button(
                    "Add new Todo",
                    icon="add",
                    on_click=lambda: self.create_todo(
                        title.value, description.value, is_active.value
                    ),
                )
                with ui.link(target="/"):
                    ui.button("Return Home", icon="home")

    def create_todo(self, title: str, description: str, is_active: bool):
        self._service.insert_todo(Todo(title, description, is_active))
        ui.notify(f"Todo Created!")
