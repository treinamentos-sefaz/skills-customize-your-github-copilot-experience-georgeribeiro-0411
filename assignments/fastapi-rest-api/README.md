# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI by creating CRUD endpoints, accepting structured request data, and returning appropriate HTTP status codes for successful and unsuccessful requests.

## 📝 Tasks

### 🛠️ Create and List Tasks

#### Descrição
Use the provided starter code to create endpoints for listing tasks and adding a task. Run the server and use FastAPI's interactive documentation to send requests and inspect responses.

To install the dependencies and start the server, run:

```bash
python -m pip install fastapi uvicorn
python starter-code.py
```

Open `http://127.0.0.1:8000/docs` in a browser to try the endpoints.

#### Requisitos
The completed API must:

- Return all tasks from `GET /tasks`
- Accept a task with a title and completion state in `POST /tasks`
- Assign each new task a unique ID and return the created task with status code `201`

### 🛠️ Retrieve and Update a Task

#### Descrição
Add endpoints for retrieving one task by its ID and replacing its data. Use the request model from the starter code to validate incoming task data.

#### Requisitos
The completed API must:

- Return one task from `GET /tasks/{task_id}`
- Replace a task's title and completion state with `PUT /tasks/{task_id}`
- Return status code `404` when the requested ID does not exist

### 🛠️ Delete a Task

#### Descrição
Complete the CRUD workflow by adding an endpoint that removes a task. Test the endpoint by creating a task, retrieving it, deleting it, and trying to retrieve it again.

#### Requisitos
The completed API must:

- Delete a task with `DELETE /tasks/{task_id}`
- Return status code `204` after a successful deletion
- Return status code `404` when asked to delete a task that does not exist