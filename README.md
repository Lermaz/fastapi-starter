# FastAPI Testing Project

A modern FastAPI project with best practices, testing, and development tools.

## Features

- FastAPI with modern Python features
- Pydantic models for data validation
- Comprehensive testing setup
- Development tools (black, isort, flake8, mypy)
- Environment variable management
- API documentation with Swagger UI

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the development server:

```bash
uvicorn app.main:app --reload
```

4. Access the API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

- Format code: `black .`
- Sort imports: `isort .`
- Lint code: `flake8`
- Type checking: `mypy .`
- Run tests: `pytest`

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── endpoints/
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   └── __init__.py
│   └── schemas/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_api/
├── .env.example
├── .gitignore
├── pyproject.toml
└── requirements.txt
```
