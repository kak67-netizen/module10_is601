# Module 10: Secure User Model, Validation, Database Testing, and Docker Deployment

## Overview

This project builds on the FastAPI and PostgreSQL application from Module 9 by adding a secure SQLAlchemy user model, Pydantic validation, password hashing, database testing, and an automated CI/CD workflow.

The application uses Docker Compose to run:
- FastAPI application
- PostgreSQL database
- pgAdmin 4

GitHub Actions is used to run automated tests and build and push the Docker image to Docker Hub after the tests pass.

## Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- pwdlib / Argon2
- pgAdmin 4
- Docker
- Docker Compose
- GitHub Actions
- Pytest
- Playwright

## Secure User Model

The SQLAlchemy `User` model contains:

- `id`
- `username`
- `email`
- `password_hash`
- `created_at`

The `username` and `email` fields use unique constraints.

Passwords are hashed before being stored in the database. Plain-text passwords are never stored.

## Pydantic Schemas

The project includes two user schemas:

### UserCreate

Used when creating a user and validates:

- Username
- Email address
- Password

### UserRead

Used when returning user information.

The password and password hash are excluded from the response.

## Password Security

Password hashing and verification are handled in:

`app/auth/security.py`

The application uses secure password hashing through `pwdlib` with Argon2.

## Database

PostgreSQL runs through Docker Compose.

Local development configuration:

- Database: `fastapi_db`
- PostgreSQL username: `postgres`
- PostgreSQL password: `postgres`
- PostgreSQL hostname within Docker: `db`
- PostgreSQL port: `5432`
- pgAdmin: `http://localhost:5050`

These credentials are for local development only and should not be used in production.

## Running the Project

From the project directory, start the Docker services:

```bash
docker compose up --build -d