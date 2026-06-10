from nicegui import ui

from viewmodels.todo_viewmodel import TodoViewmodel


class AddTodoDialog(ui.dialog):
    def __init__(self, todo_vm: TodoViewmodel):
        super().__init__()
        self._todo_vm = todo_vm

    def render(self):
        with self, ui.card().classes("w-lg gap-2"):
            title = ui.input("Title:").classes("w-full")
            description = ui.textarea("Description:").classes("w-full")
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
                ui.button("Close", icon="close", on_click=self.close)

    def open(self):
        self.render()
        return super().open()

    def close(self):
        self.clear()
        return super().close()

    def _create_todo(self, title: str, description: str, is_active: bool):
        self._todo_vm.insert_todo(title, description, is_active)
