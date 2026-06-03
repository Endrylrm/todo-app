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

- <b>Frontend:</b> Python - NiceGUI
- <b>Backend:</b> Python - FastAPI
- <b>Database:</b> SQLite
- <b>Styling:</b> CSS / Tailwind CSS


## Getting Started
Make sure you have installed:

- Python (or Docker)
- pip (or uv)
- Database server (in case you want to use another database)

## Deploy

### Option 1: Docker (Recommended)
```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project folder
cd todo-app

# use Docker Compose
docker compose up -d --build
```

### Option 2: Python
```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project folder
cd todo-app

# Navigate to folder - Backend
cd backend

# Install dependencies - Backend
# using pip
py -m venv .venv
pip install -r requirements.txt

# using uv
uv add -r requirements.txt

# Start the Backend server
fastapi run ./src/todo_api/main.py

# ******** Open new terminal ********

# Navigate to folder - Frontend
cd frontend

# Install dependencies - Frontend
# using pip
py -m venv .venv
pip install -r requirements.txt

# using uv
uv add -r requirements.txt

# Start the Frontend server
# using python
py run ./src/todo_gui/main.py

# using uv
uv run ./src/todo_gui/main.py
```

## Project Structure

```text
backend/                                    # FastAPI + SQLite
├─── database/
│    └─── todo.db					        # Todo - SQLite Database
├─── src/
│    ├─── todo_api/
│    │    ├─── controllers/
│    │    │ 	  └─── todo_controller.py	# Controller - Todo API routing and controlling
│    │    ├─── models/
│    │    │ 	  └─── todo.py		        # Model - Todo Model
│    │    ├─── repositories/
│    │    │ 	  └─── todo_repository.py	# Repository - Todo Database
│    │    ├─── services/
│    │    │ 	  └─── todo_service.py		# Service - Gets Data from todo Repository
│    │    ├─── validations/
│    │    │ 	  └─── results.py	        # SQL Validation results
│    │    └─── main.py					    # FastAPI - Entrypoint
└─── tests/                                 # tests

frontend/                                   # NiceGui Frontend
├─── src/
│    ├─── todo_api/
│    │    ├─── components/
│    │    │ 	  └─── todo_card.py	        # Card Component - The Todo that is show to the user
│    │    ├─── models/
│    │    │ 	  └─── todo.py		        # Model - Todo Model
│    │    ├─── pages/
│    │    │ 	  ├─── add_todo_page.py	    # This page is show when we click the add button
│    │    │ 	  ├─── edit_todo_page.py	# This page is show when we click the edit button in our card
│    │    │ 	  └─── todo_page.py         # Main Page - Shows all todos currently in our database
│    │    ├─── services/
│    │    │ 	  └─── api_service.py	    # Service - Gets and sends Data to our Todo API.
│    │    └─── main.py				        # NiceGui - Entrypoint
└─── tests/                                 # tests
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