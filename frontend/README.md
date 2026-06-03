# Todo GUI

A simple and responsive frontend application for managing tasks. This project consumes the Todo API and provides an intuitive interface for creating, updating, viewing, and deleting tasks.

This project was created for learning and educational purposes.

## Features

- View all tasks
- Create new tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as active or inactive
- Responsive user interface

## Tech Stack

- Python - NiceGui
- TailwindCSS (Comes with NiceGui)
- REST API Integration

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd <project-name>
```

### Install dependencies

```bash
# using pip
py -m venv .venv
pip install -r requirements.txt

# using uv
uv add -r requirements.txt
```

### Run the development server

```bash
# using python
py run ./src/todo_gui/main.py

# using uv
uv run ./src/todo_gui/main.py
```

The application will be available at:

```text
http://localhost:3000
```

## API Connection

Make sure the backend API is running before starting the frontend application.

Default API endpoint:

```text
http://localhost:8000/api/todos
```

Update the API URL in main.py if necessary.

## Project Structure

```text
src/
├─── todo_api/
│    ├─── components/
│    │ 	  └─── todo_card.py	        # Card Component - The Todo that is show to the user
│    ├─── models/
│    │ 	  └─── todo.py		        # Model - Todo Model
│    ├─── pages/
│    │ 	  ├─── add_todo_page.py	    # This page is show when we click the add button
│    │ 	  ├─── edit_todo_page.py	# This page is show when we click the edit button in our card
│    │ 	  └─── todo_page.py         # Main Page - Shows all todos currently in our database
│    ├─── services/
│    │ 	  └─── api_service.py	    # Service - Gets and sends Data to our Todo API.
│    └─── main.py				    # NiceGui - Entrypoint
tests/                              # tests
```

## Available Features

### Create Task

Allows users to add a new task with a title and description.

### Update Task

Edit task information and status.

### Delete Task

Remove tasks from the list.

### View Tasks

Display all tasks retrieved from the backend API.

## Future Improvements

- User authentication
- Search and filtering
- Pagination
- Task categories

## License

Distributed under the MIT License. See `LICENSE` for more information.

Copyright (c) 2026, Endryl Richard Monteiro
