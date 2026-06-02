from nicegui import ui

from models.todo import Todo

from services.api_service import APIService

from pages.todo_page import TodoPage
from pages.add_todo_page import AddTodoPage
from pages.edit_todo_page import EditTodoPage

api = APIService()


def root():
    dark = ui.dark_mode()
    dark.auto()
    ui.page_title("Todo Application")
    with ui.header():
        ui.icon("note_alt").classes("text-3xl")
        ui.label("Todo Application").classes("text-3xl")
    ui.sub_pages(
        {
            "/": lambda: TodoPage(api),
            "/add": lambda: AddTodoPage(api),
            "/edit/{id}": lambda id: EditTodoPage(id, api),
        }
    ).classes("w-full")


ui.run(root, port=3000)
