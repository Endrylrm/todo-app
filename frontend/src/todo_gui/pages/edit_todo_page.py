from nicegui import ui

from models.todo import Todo

from services.api_service import APIService


class EditTodoPage:
    def __init__(self, id: int, service: APIService):
        self._service = service

        self.render(id)

    def render(self, id: int):
        todo = self._service.get_todo(id)

        with ui.grid(columns=1).classes("w-full gap-1"):
            title = ui.input("Title:")
            title.set_value(todo.title)
            description = ui.input("Description:")
            description.set_value(todo.description)
            is_active = ui.switch("Is Active")
            is_active.set_value(todo.is_active)
            with ui.row():
                with ui.link(target="/"):
                    ui.button(
                        "Save Todo",
                        icon="save",
                        on_click=lambda: self.edit_todo(
                            id, title.value, description.value, is_active.value
                        ),
                    )
                with ui.link(target="/"):
                    ui.button("Return Home", icon="home")

    def edit_todo(self, id: int, title: str, description: str, is_active: bool):
        self._service.update_todo(id, Todo(title, description, is_active))

        ui.notify(f"Todo Updated!")
