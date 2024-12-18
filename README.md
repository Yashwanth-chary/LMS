# Library Management System API

## Description
This is a Django-based Library Management System API that allows users to manage books, authors, and borrowing records. The system also includes a Celery-powered background task to generate periodic reports on library activity. JWT-based authentication is implemented to secure the API endpoints.

---

## Features

- **Author Management:** Create, retrieve, update, and delete authors.
- **Book Management:** Create, retrieve, update, and delete books.
- **Borrow Records:** Create borrow records and mark books as returned.
- **Reports:** Generate and retrieve library activity reports using Celery tasks.
- **JWT Authentication:** Secure all endpoints with token-based authentication.
- **Swagger Documentation:** Interactive API documentation.

---

## Prerequisites

Ensure you have the following installed:

- Python (>= 3.8)
- Django (>= 4.0)
- PostgreSQL or SQLite
- Redis (for Celery backend)
- Docker (optional, for containerization)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Yashwanth-chary/LMS.git
cd library-management-system
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `**http://127.0.0.1:8000/**`.

---

## Celery Setup

1. Start the Redis server:

```bash
redis-server
```

2. Start the Celery worker:

```bash
celery -A library_management_system worker --loglevel=info
```

3. (Optional) Start the Celery beat scheduler for periodic tasks:

```bash
celery -A library_management_system beat --loglevel=info
```

---

## API Endpoints

### Authentication
- `POST /api/token/` - Obtain access and refresh tokens.
- `POST /api/token/refresh/` - Refresh access token.
- `POST /api/token/verify/` - Verify access token.

### Authors
- `GET /authors/` - List all authors.
- `POST /authors/` - Create a new author.
- `GET /authors/<id>/` - Retrieve a specific author.
- `PUT /authors/<id>/` - Update a specific author.
- `DELETE /authors/<id>/` - Delete a specific author.

### Books
- `GET /books/` - List all books.
- `POST /books/` - Add a new book.
- `GET /books/<id>/` - Retrieve a specific book.
- `PUT /books/<id>/` - Update a specific book.
- `DELETE /books/<id>/` - Delete a specific book.

### Borrow Records
- `POST /borrow/` - Create a new borrow record.
- `PUT /borrow/<id>/return/` - Mark a book as returned.

### Reports
- `GET /reports/` - Retrieve the latest report.
- `POST /reports/` - Generate a new report.

---

## Running with Docker (Optional)

1. Build and run the containers:

```bash
docker-compose up --build
```

2. Access the API at `http://127.0.0.1:8000/`.

---

## API Documentation

Swagger UI is available at `http://127.0.0.1:8000/swagger/`.

---

## Brief Explanation of Approach

1. **Models:**
   - Defined models for `Author`, `Book`, and `BorrowRecord` with appropriate relationships.
2. **API Endpoints:**
   - Used Django REST Framework ViewSets and Routers for CRUD operations.
3. **JWT Authentication:**
   - Secured all endpoints with `IsAuthenticated` and provided token-based login/logout.
4. **Background Task:**
   - Implemented Celery tasks for generating periodic reports, saving them as JSON files.
5. **Documentation:**
   - Added Swagger UI for interactive API documentation.
6. **Dockerization:**
   - Containerized the application with Docker for simplified deployment.

---

## Admin Credentials (For Deployed Version)

- **Username:** ---------
- **Password:** ---------

---

## Repository Link

[GitHub Repository](https://github.com/your-repo-link)



