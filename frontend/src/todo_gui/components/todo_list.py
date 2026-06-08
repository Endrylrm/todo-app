from nicegui import ui

from .todo_card import TodoCard

from models.todo import Todo

from viewmodels.todo_viewmodel import TodoViewmodel


class TodoList(ui.grid):
    def __init__(self, todo_vm: TodoViewmodel):
        super().__init__(columns=4)
        self.classes("w-full gap-4")

        self._todo_vm = todo_vm

        with self:
            self.render()

    @ui.refreshable
    def render(self):
        if not self._todo_vm.todos:
            ui.label(
                "No task yet, please click on 'Add Task' to add a new one"
            ).classes("text-4xl col-span-4")
        for todo in self._todo_vm.todos:
            TodoCard(todo, self._todo_vm)
