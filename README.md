# FastAPI Starter Project

A modern FastAPI starter template with SQLAlchemy, Alembic migrations, and user management endpoints.

## Features

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Alembic** - Database migration tool
- **SQLite** - Lightweight database (easily configurable for PostgreSQL/MySQL)
- **Pydantic** - Data validation using Python type hints
- **UV** - Fast Python package manager

## Quick Start

1. **Install dependencies**
   ```bash
   uv sync
   ```

2. **Activate virtual environment**
   ```bash
   source .venv/bin/activate
   ```

3. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

4. **Start the development server**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /user` - Create a new user
- `GET /users` - Get all users
- `GET /user/{id}` - Get user by ID

## Project Structure

```
├── src/
│   ├── db/
│   │   ├── base.py      # SQLAlchemy base class
│   │   └── config.py    # Database configuration
│   └── users/
│       ├── models.py    # User model
│       └── services.py  # User business logic
├── migrations/          # Alembic migration files
├── main.py             # FastAPI application entry point
└── pyproject.toml      # Project dependencies and configuration
```

## Development

### Creating Migrations

```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
```

### Running Tests

```bash
# Add your test commands here
```

## License

MIT License
