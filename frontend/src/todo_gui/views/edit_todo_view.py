from datetime import datetime, UTC

from nicegui import ui

from models.todo import Todo

from viewmodels.todo_viewmodel import TodoViewmodel

from exceptions.errors import APIError


class EditTodoView:
    def __init__(self, id: int, todo_vm: TodoViewmodel):
        self._todo_vm = todo_vm

        self.render(id)

    def render(self, id: int):
        try:
            todo = self._todo_vm.get_todo(id)

            with ui.grid(columns=1).classes("w-full gap-1"):
                ui.input(f"Task ID:").set_value(todo.id).set_enabled(False)
                title = ui.input("Title:")
                title.set_value(todo.title)
                description = ui.input("Description:")
                description.set_value(todo.description)
                is_active = ui.checkbox("Is Active?", value=todo.is_active)
                with ui.row():
                    with ui.link(target="/"):
                        ui.button(
                            "Save Task",
                            icon="save",
                            on_click=lambda: self._edit_todo(
                                id, title.value, description.value, is_active.value
                            ),
                            color="green",
                        )
                    with ui.link(target="/"):
                        ui.button(
                            "Delete Task",
                            icon="delete",
                            color="red",
                            on_click=lambda: self._delete_todo(id),
                        )
                    ui.space()
                    with ui.link(target="/"):
                        ui.button("Return Home", icon="home")
        except APIError as error:
            if error.status_code == 404:
                with ui.grid(columns=1).classes("w-full gap-4 place-items-center"):
                    ui.label(error.msg).classes("text-5xl")
                    with ui.link(target="/"):
                        ui.button("Return Home", icon="home")
            else:
                with ui.grid(columns=1).classes("w-full gap-4 place-items-center"):
                    ui.label("Unexpected error, try again...").classes("text-5xl")
                    with ui.link(target="/"):
                        ui.button("Return Home", icon="home")

    def _edit_todo(self, id: int, title: str, description: str, is_active: bool):
        self._todo_vm.update_todo(
            Todo(id, title, description, is_active, datetime.now(UTC))
        )
        ui.notify(f"Task with id: {id} Updated!", type="warning")

    def _delete_todo(self, id: int):
        self._todo_vm.delete_todo(id)
        ui.notify(f"Task with id: {id} Deleted!", type="negative")
