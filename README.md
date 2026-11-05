# Task Manager API

![CI](https://github.com/GabrielBorges240/task-manager-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A RESTful task management API built with FastAPI, PostgreSQL, Docker, and JWT authentication. The project applies modern backend practices: async database access, migrations, automated tests, and continuous integration.

**Live demo:** https://task-manager-api-dsle.onrender.com/docs

> The demo runs on Render's free tier. If the service is idle, the first request may take around a minute to respond.

## Tech Stack

- **FastAPI**: high-performance async web framework
- **PostgreSQL**: relational database
- **SQLAlchemy (async)**: async ORM
- **Alembic**: database migrations
- **JWT**: stateless authentication
- **Docker & Docker Compose**: containerized environment
- **Pytest**: automated tests with coverage reports
- **GitHub Actions**: continuous integration (CI)

## Features

- User registration and login with JWT
- Full CRUD for tasks
- Filtering by status, priority, and completion state
- Paginated listings
- Protected routes and per-user data isolation: each user can only access their own tasks (BOLA prevention)
- Integration tests with coverage reports

## Architecture

The code is split into layers to separate responsibilities:

- `routers/`: handle HTTP requests and responses
- `services/`: business logic
- `repositories/`: database access
- `schemas/`: input and output validation (Pydantic)
- `models/`: database models (SQLAlchemy)

## Getting Started

### Using Docker (recommended)

```bash
git clone https://github.com/GabrielBorges240/task-manager-api.git
cd task-manager-api

cp .env.example .env
docker compose up -d
docker compose exec api alembic upgrade head
```

Interactive API docs: http://localhost:8000/docs

### Local development

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

## Environment Variables

Copy `.env.example` to `.env` and adjust the values. Never commit your `.env` file.

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection URL |
| `SECRET_KEY` | Secret used to sign JWT tokens |
| `ALGORITHM` | JWT algorithm (e.g. `HS256`) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time |

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Create a new account |
| POST | `/auth/login` | Authenticate and get an access token |

### Users

| Method | Endpoint | Description |
|---|---|---|
| GET | `/users/me` | Get the current user's profile |
| PATCH | `/users/me` | Update the current user's profile |

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create a task |
| GET | `/tasks` | List the user's tasks (filters and pagination) |
| GET | `/tasks/{id}` | Get a task by ID |
| PATCH | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Usage Example

```bash
# 1. Register
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Gabriel", "email": "gabriel@email.com", "password": "123456"}'

# 2. Log in and copy the access_token
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "gabriel@email.com", "password": "123456"}'

# 3. Create a task
curl -X POST http://localhost:8000/tasks \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Study FastAPI", "priority": "high"}'

# 4. List pending tasks
curl "http://localhost:8000/tasks?status=pending&page=1&limit=20" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Running Tests

```bash
pytest tests/ -v --cov=app --cov-report=term-missing
```

## Project Structure

```
task-manager-api/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── routers/
│   └── services/
├── tests/
├── alembic/
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/
```

## Roadmap

- Refresh tokens and logout
- Rate limiting
- Text search and sorting on listings
- Automated deployment (CD)

## License

Distributed under the MIT License.

## Author

**Gabriel Borges**
Python backend developer focused on APIs, software architecture, and best practices.

[GitHub](https://github.com/GabrielBorges240)
