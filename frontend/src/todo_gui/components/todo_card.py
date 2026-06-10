from nicegui import ui

from .edit_todo_dialog import EditTodoDialog

from models.todo import Todo

from viewmodels.todo_viewmodel import TodoViewmodel


class TodoCard(ui.card):
    def __init__(self, todo: Todo, todo_vm: TodoViewmodel):
        super().__init__()
        self.classes("col-span-4 md:col-span-2 lg:col-span-1")
        self.tight()

        self._todo_vm = todo_vm
        self.todo = todo
        self.editDialog = EditTodoDialog(self.todo.id, self._todo_vm)

        self.render()

    def render(self):
        with self:
            with ui.card_section().classes("gap-2"):
                ui.label(f"Task ID: {self.todo.id}")
                ui.label(f"Title: {self.todo.title}")
                ui.label(f"Description: {self.todo.description}")
                ui.checkbox("Is Active?", value=self.todo.is_active).set_enabled(False)
                with ui.row():
                    ui.button(
                        icon="edit",
                        on_click=lambda: self.editDialog.open(),
                    )
                    ui.button(
                        on_click=lambda: self._delete_todo(),
                        icon="delete",
                        color="red-800",
                    )

    def _delete_todo(self):
        self._todo_vm.delete_todo(self.todo.id)
        self.delete()
