from nicegui import ui

from components.todo_card import TodoCard

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
        with ui.grid(columns=4).classes("w-full gap-4"):
            if not self._todo_vm.todos:
                ui.label(
                    "No task yet, please click on 'Add Task' to add a new one"
                ).classes("text-4xl col-span-4")
            for todo in self._todo_vm.todos:
                TodoCard(todo, self._todo_vm)
