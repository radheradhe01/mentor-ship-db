# Mentorship Platform Microservice

This project is a FastAPI microservice for a mentorship platform, using PostgreSQL as the database. It supports mentor/mentee management, sessions, reviews, and is ready for future AI features.

---

## Features
- FastAPI backend (async, production-ready)
- PostgreSQL database (Dockerized)
- SQLAlchemy ORM models
- Modular routers and CRUD logic
- Ready for AI features (profile vectors, chat, etc.)

---

## Prerequisites
- Python 3.9+
- Docker & Docker Compose

---

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd mentorship-db
```

### 2. Start PostgreSQL with Docker Compose
```sh
docker-compose up -d
```
This will start a PostgreSQL server on port 5432 with the correct user, password, and database.

### 3. Create a Python Virtual Environment & Install Dependencies
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install 'pydantic[email]'
```

### 4. Initialize the Database Tables
Run the provided script to create all tables:
```sh
python app/create_db.py
```

### 5. Run the FastAPI Server
```sh
uvicorn app.main:app --reload
```

- The API will be available at: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

---

## Example: Create a User

POST to `/users/` with JSON body:
```json
{
  "email": "user@example.com",
  "name": "string",
  "avatar_url": "string",
  "user_type": "mentor",
  "password": "string"
}
```

---

## Troubleshooting
- **Cannot connect to database:**
  - Make sure Docker is running and `docker-compose up -d` has started the `db` service.
  - If running FastAPI locally, ensure `app/database.py` uses `localhost` as the DB host.
- **Table does not exist:**
  - Run `python app/init_db.py` to create tables.
- **Email validation error:**
  - Run `pip install 'pydantic[email]'` in your virtual environment.

---

## Next Steps
- Add more routers and CRUD logic for other tables (mentors, mentees, sessions, etc.)
- Add authentication and authorization
- Use Alembic for migrations in production
- Add tests and CI/CD

---

## License
MIT
