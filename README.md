# CRUD with FastAPI

## What This Is
This is a lightweight RESTful API backend built with Python and FastAPI. It provides standard CRUD (Create, Read, Update, Delete) functionality to demonstrate how to handle API routing, data validation, and basic request handling within a modern Python application. 

---

## How to Install & Run
You can install all necessary dependencies and launch the development server using the following single, chained command from the root of your project repository:

```bash
pip install -r backend/requirements.txt && uvicorn backend.app.main:app --reload
```
*Note: This command installs the packages listed in your requirements file and immediately spins up the FastAPI server with hot-reloading enabled. The API will be accessible at `http://127.0.0.1:8000`.*

---

## Endpoints

Below is the routing table for the standard CRUD operations available in this API.

| HTTP Method | Endpoint        | Description                                  |
|-------------|-----------------|----------------------------------------------|
| **GET**     | `/tasks/`       | Retrieve a list of all existing tasks        |
| **GET**     | `/tasks/{id}`   | Fetch the details of a specific item by ID   |
| **POST**    | `/tasks/`       | Create and save a new item                   |
| **PUT**     | `/tasks/{id}`   | Update an existing item entirely via its ID  |
| **DELETE**  | `/tasks/{id}`   | Delete a specific item from the database     |

*(Note: If your main module routes use a different resource name like `/items/`, swap `/tasks/` accordingly.)*

---

## Example Request & Output

Here is an example of what an HTTP response looks like when fetching a single item using the API. 

**Command:**
```bash
curl -i http://127.0.0.1:8000/items/1
```

**Output:**
```http
HTTP/1.1 200 OK
date: Thu, 16 Jul 2026 15:29:01 GMT
server: uvicorn
content-length: 53
content-type: application/json

{
  "id": 1,
  "name": "Test Entry",
  "description": "Example data"
}
```

# Screenshots

## API Endpoints

![end_points](images/end_points.png)

---
## Health Check

![health_check](images/health_check.png)

---

## Get Tasks

![get_tasks](images/get_tasks.png)

---

## Get Task by Id

![get_task_id](images/get_task_id.png)

---

## Create Task

![create_task](images/create_task.png)

---

## Update Task

![update_task_input](images/update_task_input.png)

![update_task](images/update_task.png)

---
## Delete Task

![delete_task](images/delete_task.png)