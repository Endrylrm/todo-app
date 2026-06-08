from nicegui import ui

from components.todo_list import TodoList

from viewmodels.todo_viewmodel import TodoViewmodel


class TodoView:
    def __init__(self, todo_vm: TodoViewmodel):
        self._todo_vm = todo_vm
        self._todo_vm.get_todos()
        self.render()

    def render(self):
        with ui.row():
            with ui.link(target="/add"):
                ui.button("Add Task", icon="add", color="green")
        TodoList(self._todo_vm)
