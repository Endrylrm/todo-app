from nicegui import ui

from models.todo import Todo

from services.api_client_service import APIClientService

from exceptions.errors import APIError


class EditTodoPage:
    def __init__(self, id: int, api_client: APIClientService):
        self._api_client = api_client

        self.render(id)

    def render(self, id: int):
        try:
            todo = self._api_client.get_todo(id)

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
                            color="green",
                        )
                    with ui.link(target="/"):
                        ui.button(
                            "Delete Todo",
                            icon="delete",
                            color="red",
                            on_click=lambda: self.delete_todo(id),
                        )
                    ui.space()
                    with ui.link(target="/"):
                        ui.button("Return Home", icon="home")
        except APIError as e:
            if e.status_code == 404:
                with ui.grid(columns=1).classes("w-full gap-4 place-items-center"):
                    ui.label("Todo not found!").classes("text-5xl")
                    with ui.link(target="/"):
                        ui.button("Return Home", icon="home")
            else:
                with ui.grid(columns=1).classes("w-full gap-4"):
                    ui.label("Unexpected error, try again...").classes("text-5xl")
                    with ui.link(target="/"):
                        ui.button("Return Home", icon="home")

    def edit_todo(self, id: int, title: str, description: str, is_active: bool):
        self._api_client.update_todo(id, Todo(title, description, is_active))

        ui.notify(f"Todo Updated!")

    def delete_todo(self, id: int):
        self._api_client.delete_todo(id)
