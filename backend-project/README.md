# Data Extraction Backend API

This project is a **Django-based backend application** that implements an **asynchronous, job-based data extraction workflow**.
Users can start extraction jobs, track their status, retrieve results, cancel running jobs, and remove completed jobs using REST APIs.

The project is documented using **Swagger (OpenAPI 3.0)** and follows Django best practices.

---

## Features

- Asynchronous job-based workflow
- UUID-based job identification
- Job lifecycle management (pending → running → completed)
- RESTful API endpoints
- Swagger / OpenAPI documentation
- Environment-based configuration using `.env`
- Django Admin panel support

---

## Tech Stack

- Python 3.13+
- Django 6.0
- Django REST Framework
- drf-spectacular (Swagger / OpenAPI)
- SQLite (default database)

---

## Project Structure

```
backend-project/
├── src/
│   ├── config/        # Project settings, URLs, Swagger config
│   ├── health/        # Health check API
│   ├── jobs/          # Job model and admin registration
│   ├── scans/         # Scan APIs, async execution, results
│   ├── manage.py
│   └── db.sqlite3
├── .env.example       # Environment variable template
├── requirements.txt   # Python dependencies
└── README.md
```

---

## Setup Instructions (Step-by-Step)

### 1. Clone the Repository

```bash
git clone https://github.com/tanishxdev/Springer-Teams.git
cd backend-project
```

---

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Environment Configuration

Create a `.env` file in the **project root** using `.env.example`.

```env
DEBUG=True
SECRET_KEY=dev-secret-key-change-later
ALLOWED_HOSTS=127.0.0.1,localhost
```

> `.env` is ignored by Git.
> `.env.example` is provided for reference.

---

### 5. Apply Database Migrations

```bash
cd src
python manage.py migrate
```

---

### 6. Run the Development Server

```bash
python manage.py runserver
```

The server will start at:

```
http://127.0.0.1:8000/
```

---

## API Documentation (Swagger)

Swagger UI is available at:

```
http://127.0.0.1:8000/api/docs/
```

OpenAPI schema endpoint:

```
http://127.0.0.1:8000/api/schema/
```

---

## API Usage Guide

### 1. Health Check

```
GET /api/v1/health/
```

Used to verify server health.

---

### 2. Start a Scan Job

```
POST /api/v1/scan/start/
```

**Response**

```json
{
  "job_id": "uuid",
  "status": "pending"
}
```

---

### 3. Check Job Status

```
GET /api/v1/scan/status/{job_id}/
```

Returns current job status.

---

### 4. Get Scan Result

```
GET /api/v1/scan/result/{job_id}/
```

- Returns result **only after job completion**
- If job is not completed, an error response is returned

---

### 5. Cancel a Job

```
POST /api/v1/scan/cancel/{job_id}/
```

Cancels a running or pending job.

---

### 6. Remove a Job

```
DELETE /api/v1/scan/remove/{job_id}/
```

Deletes job and related result data.

---

## Async Job Execution Logic

- Jobs are executed asynchronously using background threads
- Status flow:

```
pending → running → completed
```

- Results are stored once execution finishes

This simulates real-world async processing without external task queues.

---

## Admin Panel (Optional)

Create an admin user:

```bash
python manage.py createsuperuser
```

Admin panel URL:

```
http://127.0.0.1:8000/admin/
```

---

## Evaluation Notes

This project demonstrates:

- Correct Django project setup
- Proper use of models and REST APIs
- Async job handling logic
- Swagger/OpenAPI documentation
- Environment-based configuration
- Clean and readable code structure

---

## Future Improvements (Optional)

- Replace thread-based async execution with Celery + Redis
- Add authentication and authorization
- Add pagination and filtering
- Use PostgreSQL for production environments

---

## Author

**Tanish Kumar**
Backend Engineering Intern Project
