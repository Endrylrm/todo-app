# Todo Application

A simple and efficient task management application designed to help users organize their daily activities, track progress, and improve productivity.

This project was developed to practice and demonstrate modern web development concepts, including state management, API integration, CRUD operations, and clean code principles.

## Features

- Create new tasks
- Edit existing tasks
- Mark tasks as active or inactive
- Delete tasks
- Responsive and user-friendly interface
- Data persistence

## Tech Stack

| Layer | Tools |
|-------|--------|
| **Frontend** | NiceGUI, requests |
| **Backend** | FastAPI |
| **Database** | SQLite or PostgreSQL |
| **Styling** | CSS, Tailwind CSS |


## Getting Started
Make sure you have installed:

- Python (or Docker)
- pip (or uv)
- Database server (in case you want to use another database)

## Installation

### Option 1: Docker (Recommended)

#### - Clone the repository:
```bash
git clone <repository-url>
```

#### - Navigate to project folder:
```bash
cd todo-app
```

#### - use Docker Compose to build and deploy:
```bash
docker compose up -d --build
```

### Option 2: Manual deploy

#### - Clone the repository:
```bash
git clone <repository-url>
```

#### - Navigate to Backend folder:
```bash
cd todo-app/backend
```

#### - Install dependencies - Backend:
```bash
# using pip
py -m venv .venv
pip install -r requirements.txt

# using uv
uv add -r requirements.txt
```

#### - Start the Backend server:
```bash
fastapi run ./src/todo_api/main.py
```

#### - Open a new terminal and navigate to Frontend Folder:
```bash
cd /path/to/folder/todo-app/frontend
```

#### - Install dependencies - Frontend:
```bash
# using pip
py -m venv .venv
pip install -r requirements.txt

# using uv
uv add -r requirements.txt
```

#### - Start the Frontend server:
```bash
# using python
py run ./src/todo_gui/main.py

# using uv
uv run ./src/todo_gui/main.py
```

## Project Structure

```text
backend/                                        # FastAPI + SQLite
├─── database/
│    └─── todo.db					            # Todo - SQLite Database
├─── src/
│    ├─── todo_api/
│    │    ├─── controllers/
│    │    │    └─── todo_controller.py	        # Controller - Todo API routing and controlling
│    │    ├─── databases/
│    │    │    ├─── base_db.py                      # Base Database Interface
│    │    │    ├─── postgres_db.py                  # Database - PostgreSQL connection and initialization
│    │    │    └─── sqlite.py	                    # Database - SQLite connection and initialization
│    │    ├─── dto/
│    │    │    ├─── requests.py                     # DTO Requests - Create, Update and Replace
│    │    │    └─── responses.py	                # DTO Responses - Main Object Response
│    │    ├─── exceptions/
│    │    │    └─── errors.py		                # All exceptions related to Todos
│    │    ├─── models/
│    │    │    └─── todo.py		                    # Model - Todo Model
│    │    ├─── repositories/
│    │    │    ├─── todo_postgres_repository.py     # Repository - Todo PostgreSQL Database
│    │    │    ├─── todo_repository.py              # Repository Interface - Todo Database
│    │    │    └─── todo_sqlite_repository.py	    # Repository - Todo SQLite Database
│    │    ├─── services/
│    │    │    └─── todo_service.py		            # Service - Gets Data from todo Repository
│    │    └─── main.py					            # FastAPI - Entrypoint
├─── tests/                                         # tests
└─── .env                                           # Enviroment Variables

frontend/                                           # NiceGUI + requests
├─── src/
│    ├─── todo_api/
│    │    ├─── components/
│    │    │    ├─── add_todo_dialog.py	            # This dialog is show when we click the add button
│    │    │    ├─── edit_todo_dialog.py	            # This dialog is show when we click the edit button in our card
│    │    │    ├─── todo_list.py	                # List Component - holds every Todo Card
│    │    │    └─── todo_card.py	                # Card Component - The Todo that is show to the user
│    │    ├─── events/
│    │    │    └─── todo.py		                    # All events related to Todos, from creating to deleting
│    │    ├─── exceptions/
│    │    │    └─── errors.py		                # All exceptions related to API
│    │    ├─── models/
│    │    │    └─── todo.py		                    # Model - Todo Model
│    │    ├─── services/
│    │    │    └─── api_client_service.py	        # Service - Gets and sends Data to our Todo API
│    │    ├─── viewmodels/
│    │    │    └─── todo_viewmodel.py	            # Todo Viewmodel - Manages UI State and a Bridge to our API
│    │    ├─── views/
│    │    │    └─── todo_view.py                    # Main View - Shows all todos currently in our database
│    │    └─── main.py				                # NiceGui - Entrypoint
├─── tests/                                         # tests
└─── .env                                           # Enviroment Variables
```

## Future Improvements

- User authentication and authorization
- Filter tasks by status
- Task categories and labels
- Due dates and reminders
- Task sharing and collaboration
- Drag-and-drop task organization
- Add SQLAlchemy for database agnostic code

## License

Distributed under the MIT License. See `LICENSE` in the backend and frontend projects for more information.

Copyright (c) 2026, Endryl Richard Monteiro