from nicegui import ui

from models.todo import Todo
from services.api_service import APIService


class TodoCard(ui.card):
    def __init__(self, index: int, todo: Todo, service: APIService):
        super().__init__()
        self.classes("col-span-4 md:col-span-2 lg:col-span-1")
        self.tight()

        self._service = service

        self.title = todo.title
        self.description = todo.description
        self.is_active = todo.is_active

        with self:
            with ui.card_section().classes("gap-2"):
                ui.label(f"Title: {self.title}")
                ui.label(f"Description: {self.description}")
                ui.switch("Is Active", value=self.is_active).set_enabled(False)
                with ui.row():
                    with ui.link(target=f"/edit/{index}"):
                        ui.button(icon="edit")
                    ui.button(
                        on_click=lambda: self.delete_todo(index),
                        icon="delete",
                        color="red-800",
                    )

    def delete_todo(self, id: int):
        self._service.todos.pop(str(id), None)
        self.delete()
