
# Module 9: Working with Raw SQL in pgAdmin

## Overview
This project demonstrates how to create and manage a PostgreSQL database using raw SQL commands in pgAdmin.

Docker Compose is used to run three services:
- FastAPI application
- PostgreSQL database
- pgAdmin 4

## Technologies
- Python
- FastAPI
- PostgreSQL
- pgAdmin 4
- Docker Compose
- SQL

## Running the Project

From the project directory, run:

```bash
docker compose up --build -d
```

Check that the containers are running:

```bash
docker compose ps
```

Open:
- FastAPI: http://localhost:8000
- pgAdmin: http://localhost:5050

## Database Configuration

The Docker Compose configuration uses the following local development credentials:

- Database: `fastapi_db`
- PostgreSQL username: `postgres`
- PostgreSQL password: `postgres`
- pgAdmin email: `admin@example.com`
- pgAdmin password: `admin123`
- PostgreSQL hostname within Docker: `db`
- PostgreSQL port: `5432`

These are demonstration credentials only and should not be used in production.

## SQL Operations

The `module9_queries.sql` file demonstrates:

1. Creating the `users` and `calculations` tables
2. Inserting user and calculation records
3. Retrieving records using `SELECT`
4. Joining tables using `JOIN`
5. Updating records using `UPDATE`
6. Deleting records using `DELETE`
7. Verifying the final database records

The SQL statements should be executed in the documented order using pgAdmin's Query Tool. Do not rerun the entire script against an already populated database.

## Documentation

The `screenshots/` folder contains evidence of the SQL operations and Docker environment.

The assignment report documents the results and includes a reflection on the learning experience.
