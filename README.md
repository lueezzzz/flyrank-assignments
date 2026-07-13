# Backend Engineering : Week 2

* **Routes and Services Unchanged**: The existing router paths (`/users`) and HTTP endpoint logic were kept completely intact. No code signatures or route setups were altered to fit the database layer.
* **Direct Database Integration**: Since this project did not utilize an initial in-memory mock store, the PostgreSQL connection pool (`pg`) was introduced into the existing handlers to replace placeholder JSON logic with database queries.

---

## How to Run the Project

The entire stack builds and orchestrates with a single execution step.

### Prerequisites
- Docker and Docker Compose installed on your local environment.

### Startup Command
Run the application and database together via:
```bash
docker compose up --build