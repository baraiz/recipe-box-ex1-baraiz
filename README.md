# Recipe Box API (EX1)

A FastAPI backend microservice for managing a personal recipe collection.
This project is part of EX1 (FastAPI Foundations). 

Currently, the data layer uses an **in-memory repository** for the base grade requirements. It is architected with dependency injection to easily graduate to SQLite/SQLModel in future exercises.

## Prerequisites
- Python 3.12+
- uv package manager

## Setup Instructions
1. Clone the repository and navigate to the project directory.
2. Create the virtual environment and install dependencies using uv:
   uv venv --python 3.12
   uv sync

## Running the API Locally
Start the FastAPI server with live-reload enabled:
uv run uvicorn app.main:app --reload

## Executing the Tests
Run the test suite:
uv run pytest tests -v
