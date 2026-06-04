from nicegui import ui

from models.todo import Todo
from services.api_client_service import APIClientService


class TodoCard(ui.card):
    def __init__(self, todo: Todo, api_client: APIClientService):
        super().__init__()
        self.classes("col-span-4 md:col-span-2 lg:col-span-1")
        self.tight()

        self._api_client = api_client

        self.todo = todo

        with self:
            with ui.card_section().classes("gap-2"):
                ui.label(f"Task ID: {self.todo.id}")
                ui.label(f"Title: {self.todo.title}")
                ui.label(f"Description: {self.todo.description}")
                ui.checkbox("Is Active?", value=self.todo.is_active).set_enabled(False)
                with ui.row():
                    with ui.link(target=f"/edit/{self.todo.id}"):
                        ui.button(icon="edit")
                    ui.button(
                        on_click=lambda: self._delete_todo(),
                        icon="delete",
                        color="red-800",
                    )

    def _delete_todo(self):
        self._api_client.delete_todo(self.todo.id)
        ui.notify(f"Task with id: {self.todo.id} Deleted!")
        self.delete()
