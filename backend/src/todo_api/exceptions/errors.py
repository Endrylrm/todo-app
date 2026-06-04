class TodoNotFoundError(Exception):
    def __init__(self, id: int):
        self.id = id
        self().__init__(f"Todo with id: {self.id} not found!")


class TodoInvalidDataError(Exception):
    def __init__(self, variable: str):
        self.variable = variable
        self().__init__(f"No '{self.variable}' in request!")


class TodoEmptyDataError(Exception):
    def __init__(self):
        self.msg = "The request body should not be empty"
        super().__init__(self.msg)
