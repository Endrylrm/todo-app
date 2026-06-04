import os
from dotenv import load_dotenv

load_dotenv()

from nicegui import ui

from models.todo import Todo

from services.api_client_service import APIClientService

from pages.todo_page import TodoPage
from pages.add_todo_page import AddTodoPage
from pages.edit_todo_page import EditTodoPage

API_URL = os.getenv("API_URL", "http://localhost:8000/api/todos")
api_client = APIClientService(API_URL)


def root():
    dark = ui.dark_mode()
    dark.auto()
    ui.page_title("Todo Application")
    with ui.header():
        ui.icon("note_alt").classes("text-3xl")
        ui.label("Todo Application").classes("text-3xl")
    ui.sub_pages(
        {
            "/": lambda: TodoPage(api_client),
            "/add": lambda: AddTodoPage(api_client),
            "/edit/{id}": lambda id: EditTodoPage(id, api_client),
        }
    ).classes("w-full")


ui.run(root, port=3000)
