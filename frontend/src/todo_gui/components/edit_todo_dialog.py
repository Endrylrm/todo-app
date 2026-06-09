from datetime import datetime, UTC

from nicegui import ui

from models.todo import Todo

from viewmodels.todo_viewmodel import TodoViewmodel

from exceptions.errors import APIError


class EditTodoDialog(ui.dialog):
    def __init__(self, id: int, todo_vm: TodoViewmodel):
        super().__init__()
        self._todo_vm = todo_vm

        try:
            todo = self._todo_vm.get_todo(id)

            with self, ui.card().classes("w-lg gap-2"):
                title = ui.input("Title:").classes("w-full")
                title.set_value(todo.title)
                description = ui.textarea("Description:").classes("w-full")
                description.set_value(todo.description)
                is_active = ui.checkbox("Is Active?", value=todo.is_active)
                with ui.row():
                    ui.button(
                        "Save Task",
                        icon="save",
                        on_click=lambda: self._edit_todo(
                            id, title.value, description.value, is_active.value
                        ),
                        color="green",
                    )
                    ui.button(
                        "Delete Task",
                        icon="delete",
                        on_click=lambda: self._delete_todo(id),
                        color="red",
                    )
                    ui.button("Close", icon="close", on_click=self.delete)
        except APIError as error:
            if error.status_code == 404:
                with self, ui.card().classes("w-lg gap-2"):
                    ui.label(error.msg).classes("text-5xl")
                    ui.button("Close", icon="close", on_click=self.delete)
            else:
                with self, ui.card().classes("w-lg gap-2"):
                    ui.label("Unexpected error, try again...").classes("text-5xl")
                    ui.button("Close", icon="close", on_click=self.delete)

    def _edit_todo(self, id: int, title: str, description: str, is_active: bool):
        self._todo_vm.update_todo(
            Todo(id, title, description, is_active, datetime.now(UTC))
        )
        self.delete()

    def _delete_todo(self, id: int):
        self._todo_vm.delete_todo(id)
        self.delete()
