class TodoNotFoundError(Exception):
    def __init__(self, id: int):
        self.id = id


class TodoInvalidDataError(Exception):
    def __init__(self, variable: str):
        self.variable = variable


class TodoEmptyDataError(Exception):
    def __init__(self):
        self.message = "The request body should not be empty"
