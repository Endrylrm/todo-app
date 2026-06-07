import os
from dotenv import load_dotenv

load_dotenv()

from nicegui import ui

from models.todo import Todo

from services.api_client_service import APIClientService

from viewmodels.todo_viewmodel import TodoViewmodel

from views.todo_view import TodoView
from views.add_todo_view import AddTodoView
from views.edit_todo_view import EditTodoView

API_URL = os.getenv("API_URL", "http://localhost:8000/api/todos")
api_client = APIClientService(API_URL)
todo_vm = TodoViewmodel(api_client)


def root():
    dark = ui.dark_mode()
    dark.auto()
    ui.page_title("Todo Application")
    with ui.header():
        ui.icon("note_alt").classes("text-3xl")
        ui.label("Todo Application").classes("text-3xl")
    ui.sub_pages(
        {
            "/": lambda: TodoView(todo_vm),
            "/add": lambda: AddTodoView(todo_vm),
            "/edit/{id}": lambda id: EditTodoView(id, todo_vm),
        }
    ).classes("w-full")


ui.run(root, port=3000)
