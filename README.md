# FastAPI Best Practices Skeleton

A minimal, modular FastAPI project with best practices for structure, database, and testing.

## Features

- **FastAPI** app with modular routers (`/auth`, `/posts`)
- **SQLAlchemy** models and PostgreSQL support
- **Pydantic** schemas for data validation
- **Alembic** for database migrations
- **Pytest** and **httpx** for async testing
- **Ruff** for linting
- Configurable logging

## Project Structure

```
src/
  main.py           # FastAPI app entrypoint
  database.py       # SQLAlchemy setup
  auth/             # Auth module (router, models, schemas)
  posts/            # Posts module (router, models, schemas)
alembic/            # Alembic migrations
tests/              # Pytest tests for each module
requirements/       # Dependency files
logging.ini         # Logging config
alembic.ini         # Alembic config
```

## Quickstart

1. **Install dependencies**

   ```bash
   pip install -r requirements/dev.txt
   ```

2. **Set up the database**

   - Default: PostgreSQL (see `src/database.py` and `alembic.ini` for connection strings)
   - Create your DB and update `DATABASE_URL` env var if needed

3. **Run migrations**

   ```bash
   alembic upgrade head
   ```

4. **Run the app**

   ```bash
   uvicorn src.main:app --reload
   ```

5. **Run tests**
   ```bash
   pytest
   ```

## API Overview

- **/auth/ping**: Health check for auth
- **/posts/ping**: Health check for posts

## Models

- **User**: `id`, `username`
- **Post**: `id`, `title`

## Dev & Linting

- Lint: `ruff .`
- Logging: see `logging.ini` for format and level

## Migrations

- Alembic scripts in `alembic/versions/`
- Config in `alembic.ini` and `alembic/env.py`
