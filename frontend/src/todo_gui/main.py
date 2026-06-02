from nicegui import ui

todos = {}

for index in range(1, 11):
    todos.update(
        {
            f"{index}": {
                "title": f"Test Todo {index}",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ut finibus dui. Maecenas vitae dolor ac lacus volutpat iaculis. Sed eleifend tristique felis a egestas. Donec sed faucibus sem.",
                "is_active": True,
            }
        }
    )


def root():
    dark = ui.dark_mode()
    dark.auto()
    ui.page_title("Todo Application")
    with ui.header():
        ui.icon("note_alt").classes("text-3xl")
        ui.label("Todo Application").classes("text-3xl")
    ui.sub_pages(
        {
            "/": todo_page,
            "/add": add_todo_page,
            "/edit/{id}": edit_todo_page,
        }
    ).classes("w-full")


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
                with ui.link(target=f"/edit/{index}"):
                    ui.button(icon="edit")
                ui.button(
                    on_click=lambda: delete_todo(index), icon="delete", color="red-800"
                )


def new_todo(title: str, description: str, is_active: bool):
    new_key = str(int(list(todos.keys())[-1]) + 1)
    todos.update(
        {
            new_key: {
                "title": title,
                "description": description,
                "is_active": is_active,
            }
        }
    )
    ui.notify(f"Todo Created {new_key}")


def edit_todo(id: int, title: str, description: str, is_active: bool):
    todos[str(id)].update(
        {"title": title, "description": description, "is_active": is_active}
    )
    ui.notify(f"Todo Updated {id}")


def edit_todo_page(id: int):
    with ui.grid(columns=1).classes("w-full gap-1"):
        title = ui.input("Title:")
        title.set_value(todos[str(id)]["title"])
        description = ui.input("Description:")
        description.set_value(todos[str(id)]["description"])
        is_active = ui.switch("Is Active")
        is_active.set_value(todos[str(id)]["is_active"])
        with ui.row():
            with ui.link(target="/"):
                ui.button(
                    "Save Todo",
                    icon="save",
                    on_click=lambda: edit_todo(
                        id, title.value, description.value, is_active.value
                    ),
                )
            with ui.link(target="/"):
                ui.button("Return Home", icon="home")


def add_todo_page():
    with ui.grid(columns=1).classes("w-full gap-1"):
        title = ui.input("Title:")
        description = ui.input("Description:")
        is_active = ui.switch("Is Active")
        with ui.row():
            ui.button(
                "Add new Todo",
                icon="add",
                on_click=lambda: new_todo(
                    title.value, description.value, is_active.value
                ),
            )
            with ui.link(target="/"):
                ui.button("Return Home", icon="home")


def todo_page():
    with ui.row():
        with ui.link(target="/add"):
            ui.button("Add Todo", icon="add")
    with ui.grid(columns=4).classes("w-full gap-4"):
        for todo in todos:
            create_todo_card(todo, todos[todo])


ui.run(root)
