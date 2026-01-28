# Personal Finance Backend API

A production-ready backend API for managing personal finance data, built with Python and FastAPI.
This project demonstrates the design and implementation of a real-world backend system for managing users, accounts, and financial transactions, with a focus on clean architecture, data modeling, and API design.

Core Features:

- User authentication and authorization (JWT)
- Account and transaction management
- Relational data modeling with PostgreSQL
- Input validation and error handling
- Pagination and filtering
- Dockerized setup for local and cloud deployment

The application follows a layered architecture:

- API layer (FastAPI routers)
- Service layer (business logic)
- Data access layer (SQLAlchemy models and repositories)
- Database (PostgreSQL)

This separation improves testability, maintainability, and clarity.

Tech Stack:

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- JWT Authentication

Design Decisions:

- FastAPI was chosen for its async support, strong typing with Pydantic, and excellent developer experience.
- PostgreSQL was used to model relational financial data with consistency guarantees.
- JWT-based authentication was implemented for stateless API access.

Optional Future Improvements:

- Role-based access control
- Background jobs for analytics
- Improved reporting endpoints

This project is fully dockerized. Follow these steps to get the environment running and the database migrated.
Build and start the container

```bash
docker-compose up --build
```

Run database migrations

```bash
docker-compose exec web alembic upgrade head
```

If you modify the models, create a new migration script with:

```bash
docker-compose exec web alembic revision --autogenerate -m "Your message here"
```

Apply the new migration with the upgrade command

```bash
docker-compose exec web alembic upgrade head
```

Useful Commands:
Check logs

```bash
docker-compose logs -f
```

Stop the containers

```bash
docker-compose down
```

Access the Database via PSQL shell

```bash
docker-compose exec db psql -U postgres -d finance_db
```
