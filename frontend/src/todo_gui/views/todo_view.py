from nicegui import ui

from components.todo_list import TodoList
from components.add_todo_dialog import AddTodoDialog

from viewmodels.todo_viewmodel import TodoViewmodel


class TodoView:
    def __init__(self, todo_vm: TodoViewmodel):
        self._todo_vm = todo_vm
        self.addDialog = AddTodoDialog(self._todo_vm)
        self.render()

    def render(self):
        with ui.row():
            ui.button(
                "Add Task",
                icon="add",
                color="green",
                on_click=lambda: self.addDialog.open(),
            )
        TodoList(self._todo_vm)
