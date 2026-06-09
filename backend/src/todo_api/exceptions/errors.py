class TodoNotFoundError(Exception):
    def __init__(self, id: int):
        self.id = id
        super().__init__(f"Todo with id: {self.id} not found!")


class TodoInvalidDataError(Exception):
    def __init__(self, variable: str):
        self.variable = variable
        super().__init__(f"No '{self.variable}' in request!")


class TodoEmptyDataError(Exception):
    def __init__(self):
        self.message = "The request body should not be empty!"
        super().__init__(self.message)


class TodoNotCreatedError(Exception):
    def __init__(self):
        self.message = "Unable to create the todo!"
        super().__init__(self.message)
