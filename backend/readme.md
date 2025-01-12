# Flask API with MySQL

This project is a simple Flask API connected to a MySQL database, built for learning purposes. It demonstrates how to structure a Flask application with database integration and how to perform basic CRUD operations using SQLAlchemy and Flask-Migrate for database migrations.

### 🚧 **Note: This is a studying project.** 🚧

This project is intended to explore Flask, SQLAlchemy, MySQL, and Flask-Migrate. It is not intended for production use.

## Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on a "Book" resource.
- **Database Integration**: Using SQLAlchemy for ORM (Object-Relational Mapping) with MySQL.
- **Environment Variables**: Sensitive data (like database URI) is managed using environment variables from a `.env` file.

## Requirements

- Python 3.x
- MySQL Database
- Docker (optional, for running MySQL in a container)
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Python-dotenv

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/flask-mysql-api.git
cd flask-mysql-api
```

### 2. Create a .env file in the root of your project nd set the following environment variables:

```bash
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=library_db
MYSQL_USER=library_user
MYSQL_PASSWORD=library_pass
DATABASE_URI=mysql+mysqlconnector://library_user:library_pass@mysql:3306/library_db
FLASK_ENV=development
```

### 2. You need to have Docker installed on your machine. Once installed, you can start the API containers with:

```bash
docker-compose up -d
```

## Endpoints

- **GET** `/books`  
  Retrieve all books from the database.

- **GET** `/books/<int:book_id>`  
  Retrieve details of a specific book by ID.

- **POST** `/books`  
  Add a new book to the database.  
  **Required fields**: `title`, `author`, `year`.

- **PUT** `/books/<int:book_id>`  
  Update the details of an existing book by ID.

- **DELETE** `/books/<int:book_id>`  
  Delete a book from the database by ID.
