# FastAPI PostgreSQL API Development

A REST API built with FastAPI, PostgreSQL, and SQLAlchemy ORM. This project demonstrates API development, database integration, and CRUD operations using Python.

## Features

* REST API development using FastAPI
* PostgreSQL database integration
* SQLAlchemy ORM for database operations
* Environment variable configuration using `.env`
* Automatic interactive API documentation
* Database session management

## Tech Stack

* **Language:** Python
* **API Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Database Driver:** Psycopg
* **Server:** Uvicorn
* **Configuration:** python-dotenv

## Project Structure

```text
.
├── main.py
├── database.py
├── models.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

Before running the project, install:

* Python
* PostgreSQL
* Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mohd-arshu/FastApi-Postgres-API-Development.git
```

### 2. Navigate to the project directory

```bash
cd FastApi-Postgres-API-Development
```

### 3. Create a virtual environment

**Windows:**

```powershell
py -m venv venv
```

### 4. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

If you're using Command Prompt instead of PowerShell:

```cmd
venv\Scripts\activate.bat
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Database Configuration

Create a PostgreSQL database for the project.

Create a `.env` file in the project root directory:

```dotenv
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
```

Replace the example values with your PostgreSQL credentials.

**Security:** Never commit your `.env` file or database credentials to GitHub.

## Run the Application

Start the FastAPI development server:

```bash
python -m uvicorn main:app --reload
```

## API Documentation

Once the application is running, access the following endpoints in your browser:

* **API Root:** http://127.0.0.1:8000/
* **Swagger UI:** http://127.0.0.1:8000/docs
* **ReDoc:** http://127.0.0.1:8000/redoc

FastAPI automatically generates interactive API documentation.

## Learning Objectives

This project is intended to develop practical skills in:

* Building REST APIs with Python
* Connecting FastAPI to PostgreSQL
* Defining database models with SQLAlchemy
* Managing database sessions
* Configuring applications using environment variables
* Using Git and GitHub for version control

## Future Improvements

* Implement complete CRUD operations
* Add request and response validation using Pydantic
* Implement authentication and authorization
* Add automated tests
* Improve error handling and logging
* Add database migrations using Alembic
* Deploy the API to a cloud platform

## Author

Mohammed Arshad

GitHub: https://github.com/mohd-arshu
