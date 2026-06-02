from models.todo import Todo


class APIService:
    def __init__(self):
        self.todos: dict[str, Todo] = {}

        for index in range(1, 11):
            self.todos.update(
                {
                    f"{index}": Todo(
                        f"Test Todo {index}",
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ut finibus dui. Maecenas vitae dolor ac lacus volutpat iaculis. Sed eleifend tristique felis a egestas. Donec sed faucibus sem.",
                        True,
                    )
                }
            )

    def get_todos(self) -> dict[str, Todo]:
        todos = {}

        return todos

    def get_todo(self, id: int) -> dict[str, Todo]:
        todo = {}

        return todo

    def insert_todo(self, todo: Todo):
        pass

    def update_todo(self, id: int, todo: Todo):
        pass

    def delete_todo(self, id: int):
        pass
