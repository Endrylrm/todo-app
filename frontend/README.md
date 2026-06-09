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
- CSS and TailwindCSS
- requests - REST API Integration

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
│    │ 	  ├─── todo_list.py	            # List Component - holds every Todo Card
│    │ 	  └─── todo_card.py	            # Card Component - The Todo that is show to the user
│    ├─── events/
│    │ 	  └─── todo.py                  # All events related to Todos, from creating to deleting
│    ├─── exceptions/
│    │ 	  └─── errors.py                # All exceptions related to API
│    ├─── models/
│    │ 	  └─── todo.py		            # Model - Todo Model
│    ├─── services/
│    │ 	  └─── api_client_service.py    # Service - Gets and sends Data to our Todo API
│    ├─── viewmodels/
│    │ 	  └─── todo_viewmodel.py        # Todo Viewmodel - Manages UI State and a Bridge to our API
│    ├─── views/
│    │ 	  ├─── add_todo_view.py	        # This view is show when we click the add button
│    │ 	  ├─── edit_todo_view.py	    # This view is show when we click the edit button in our card
│    │ 	  └─── todo_view.py             # Main View - Shows all todos currently in our database
│    └─── main.py				        # NiceGui - Entrypoint
tests/                                  # tests
.env                                    # Enviroment Variables
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
