from nicegui import ui

todos = {
    "0": {"title": "Test Todo 0", "description": "Lorem Ipsum", "is_active": True},
    "1": {"title": "Test Todo 1", "description": "Lorem Ipsum", "is_active": True},
    "2": {"title": "Test Todo 2", "description": "Lorem Ipsum", "is_active": True},
    "3": {"title": "Test Todo 3", "description": "Lorem Ipsum", "is_active": False},
    "4": {"title": "Test Todo 4", "description": "Lorem Ipsum", "is_active": True},
    "5": {"title": "Test Todo 5", "description": "Lorem Ipsum", "is_active": True},
    "6": {"title": "Test Todo 6", "description": "Lorem Ipsum", "is_active": False},
    "7": {"title": "Test Todo 7", "description": "Lorem Ipsum", "is_active": True},
    "8": {"title": "Test Todo 8", "description": "Lorem Ipsum", "is_active": True},
    "9": {"title": "Test Todo 9", "description": "Lorem Ipsum", "is_active": True},
    "10": {"title": "Test Todo 10", "description": "Lorem Ipsum", "is_active": False},
}


def root():
    dark = ui.dark_mode()
    dark.auto()
    ui.page_title("Todo Application")
    with ui.header():
        ui.icon("note_alt").classes("text-3xl")
        ui.label("Todo Application").classes("text-3xl")
    ui.sub_pages({"/": todo_page}).classes("w-full")


def create_todo_card(index: int, todo_dict: dict):
    with ui.card().tight().classes("col-span-4 md:col-span-2 lg:col-span-1") as card:

        def delete_todo(id: int):
            todos.pop(str(index), None)
            card.delete()

        with ui.card_section().classes("gap-2"):
            ui.label(f"Title: {todo_dict["title"]}")
            ui.label(f"Description: {todo_dict["description"]}")
            ui.switch("Is Active", value=todo_dict["is_active"]).set_enabled(False)
            with ui.row():
                ui.button(
                    on_click=lambda: delete_todo(index), icon="delete", color="red-800"
                )


def todo_page():
    with ui.row():
        ui.button("Add Todo", icon="add")
        ui.space()
    with ui.grid(columns=4).classes("w-full gap-4"):
        for todo in todos:
            create_todo_card(todo, todos[todo])


ui.run(root)
