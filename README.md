# Smart Campus - Ticket Management System

## Overview

**Smart Campus** is a comprehensive Django REST Framework-based API for managing support tickets in a campus environment. The application provides a robust ticket management system with features like filtering, searching, pagination, caching, and JWT authentication.

---

## 📋 Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Technology Stack](#technology-stack)
4. [Prerequisites](#prerequisites)
5. [Installation & Setup](#installation--setup)
6. [Database Configuration](#database-configuration)
7. [API Endpoints](#api-endpoints)
8. [Authentication](#authentication)
9. [API Features](#api-features)
10. [Environment Variables](#environment-variables)
11. [Usage Examples](#usage-examples)
12. [Project Architecture](#project-architecture)
13. [Key Classes & Components](#key-classes--components)
14. [Caching Strategy](#caching-strategy)
15. [Troubleshooting](#troubleshooting)
16. [Contributing](#contributing)
17. [License](#license)

---

## ✨ Features

- **Ticket Management**: Create, read, update, and delete support tickets
- **Advanced Filtering**: Filter tickets by category, priority, and other attributes
- **Search Functionality**: Full-text search across ticket titles and descriptions
- **Sorting & Ordering**: Sort tickets by any field
- **Pagination**: Configurable pagination with page-based navigation
- **Authentication**: JWT (JSON Web Token) based authentication using SimpleJWT
- **Authorization**: Permission-based access control with role-based security
- **Caching**: Redis-based caching for improved performance (60-second cache TTL)
- **Database**: PostgreSQL for robust data persistence
- **REST API**: Clean, RESTful API design following Django best practices
- **Admin Interface**: Django admin panel for easy content management

---

## 📁 Project Structure

```
smart_campus_project/
│
├── env/                                    # Python virtual environment
│   └── Lib/
│       └── site-packages/                  # Installed packages
│
└── smart_campus/                           # Main Django project directory
    │
    ├── manage.py                           # Django management script
    ├── db.sqlite3 / PostgreSQL DB          # Database file
    │
    ├── smart_campus/                       # Django project settings package
    │   ├── __init__.py
    │   ├── settings.py                     # Project configuration
    │   ├── urls.py                         # Main URL routing
    │   ├── asgi.py                         # ASGI configuration (async)
    │   ├── wsgi.py                         # WSGI configuration (production)
    │   └── __pycache__/
    │
    └── tickets/                            # Tickets app (main application)
        ├── migrations/                     # Database migrations
        │   ├── 0001_initial.py
        │   ├── 0002_remove_ticket_created_at_remove_ticket_status_and_more.py
        │   └── __init__.py
        │
        ├── __init__.py
        ├── admin.py                        # Django admin configuration
        ├── apps.py                         # App configuration
        ├── models.py                       # Database models (Ticket)
        ├── serializers.py                  # DRF serializers
        ├── permissions.py                  # Custom permission classes
        ├── views.py                        # API views/endpoints
        ├── urls.py                         # App-specific URL routing
        ├── tests.py                        # Unit tests
        └── __pycache__/
```

---

## 🛠 Technology Stack

### Core Framework
- **Django** 5.2.11 - High-level Python web framework
- **Django REST Framework** 3.16.1 - REST API development toolkit
- **Python** 3.x

### Authentication & Authorization
- **djangorestframework-simplejwt** 5.5.1 - JWT authentication
- **PyJWT** 2.11.0 - JWT encoding/decoding

### Database
- **PostgreSQL** - Primary database
- **psycopg2** 2.9.11 - PostgreSQL adapter for Python
- **sqlparse** 0.5.5 - SQL parsing utility

### Additional Libraries
- **django-filter** 25.2 - Advanced filtering for REST APIs
- **asgiref** 3.11.1 - ASGI utilities
- **tzdata** 2025.3 - timezone database

### API Features
- REST Framework & Serializers
- DjangoFilterBackend for filtering
- OrderingFilter for sorting
- SearchFilter for text search
- PageNumberPagination for pagination
- Authentication: SessionAuthentication & JWTAuthentication
- Permission: IsAuthenticated (default) & Custom permissions

---

## 📋 Prerequisites

Before setting up the project, ensure you have:

- **Python 3.8+** installed
- **PostgreSQL** installed and running
- **pip** (Python package manager)
- **Git** (for version control)
- **Virtual Environment** tool (venv, virtualenv, etc.)

---

## 🚀 Installation & Setup

### 1. Clone/Download the Project

```bash
cd path/to/smart_campus_project
```

### 2. Create & Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv env
env\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Or manually install packages:**
```bash
pip install Django==5.2.11
pip install djangorestframework==3.16.1
pip install djangorestframework-simplejwt==5.5.1
pip install django-filter==25.2
pip install psycopg2==2.9.11
pip install PyJWT==2.11.0
```

### 4. Navigate to Project

```bash
cd smart_campus
```

### 5. Configure Database Settings

Edit `smart_campus/settings.py` and update database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'helpdesk_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 8. Start Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

---

## 🗄 Database Configuration

### PostgreSQL Setup

1. **Create Database**:
```sql
CREATE DATABASE helpdesk_db;
```

2. **Create User**:
```sql
CREATE USER postgres WITH PASSWORD '2349';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET default_transaction_deferrable TO on;
ALTER ROLE postgres SET default_transaction_read_committed TO off;
GRANT ALL PRIVILEGES ON DATABASE helpdesk_db TO postgres;
```

3. **Verify Connection** in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'helpdesk_db',
        'USER': 'postgres',
        'PASSWORD': '2349',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🔌 API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|-----------------|
| POST | `/api/token/` | Obtain JWT token | Username/Password |
| POST | `/api/token/refresh/` | Refresh JWT token | Refresh Token Required |

### Ticket Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|-----------------|
| GET | `/tickets/` | List all tickets with filters | Required |
| POST | `/tickets/` | Create new ticket | Required |
| GET | `/tickets/<id>/` | Retrieve specific ticket | Required |
| PUT | `/tickets/<id>/` | Full update ticket | Required |
| PATCH | `/tickets/<id>/` | Partial update ticket | Required |
| DELETE | `/tickets/<id>/` | Delete ticket | Required |

---

## 🔐 Authentication

### JWT Authentication Flow

1. **Obtain Token**:
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

**Response**:
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

2. **Use Token in Requests**:
```bash
curl -X GET http://localhost:8000/tickets/ \
  -H "Authorization: Bearer <your_access_token>"
```

3. **Refresh Token** (when access token expires):
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token"}'
```

---

## 🎯 API Features

### 1. Filtering
Filter tickets by category:
```
GET /tickets/?category=technical
```

### 2. Search
Search tickets by title or description:
```
GET /tickets/?search=network
```

### 3. Ordering
Sort tickets by any field:
```
GET /tickets/?ordering=-priority
GET /tickets/?ordering=title
```

### 4. Pagination
Navigate through paginated results:
```
GET /tickets/?page=2
```
Default page size: 2 tickets per page

### 5. Combined Filtering
All features can be combined:
```
GET /tickets/?category=technical&search=network&ordering=title&page=2
```

---

## 🗂 Environment Variables

Create a `.env` file in the project root (optional for production):

```env
DEBUG=True
SECRET_KEY=django-insecure-your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_NAME=helpdesk_db
DATABASE_USER=postgres
DATABASE_PASSWORD=2349
DATABASE_HOST=localhost
DATABASE_PORT=5432
JWT_ALGORITHM=HS256
```

---

## 📝 Usage Examples

### 1. Get JWT Token
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "password123"}'
```

### 2. Create a Ticket
```bash
curl -X POST http://localhost:8000/tickets/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Network Outage",
    "description": "Internet connection is down in Building A",
    "category": "technical",
    "priority": "high"
  }'
```

### 3. List Tickets
```bash
curl -X GET http://localhost:8000/tickets/ \
  -H "Authorization: Bearer <token>"
```

### 4. Get Specific Ticket
```bash
curl -X GET http://localhost:8000/tickets/1/ \
  -H "Authorization: Bearer <token>"
```

### 5. Update Ticket (Full)
```bash
curl -X PUT http://localhost:8000/tickets/1/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Network Outage - RESOLVED",
    "description": "Internet connection restored",
    "category": "technical",
    "priority": "low"
  }'
```

### 6. Partial Update Ticket
```bash
curl -X PATCH http://localhost:8000/tickets/1/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"priority": "low"}'
```

### 7. Delete Ticket
```bash
curl -X DELETE http://localhost:8000/tickets/1/ \
  -H "Authorization: Bearer <token>"
```

---

## 🏗 Project Architecture

### MVC Pattern (Django Interpretation)

- **Models** (`models.py`) - Data layer defining database schema
- **Views** (`views.py`) - Business logic and API endpoints
- **Serializers** (`serializers.py`) - Data validation and transformation

### Request Flow

```
Request
   ↓
URL Router (urls.py)
   ↓
View (views.py) - Check Authentication & Permissions
   ↓
Serializer (serializers.py) - Validate Data
   ↓
Model (models.py) - Database Operations
   ↓
Cache (Redis) - Store/Retrieve
   ↓
Response (JSON)
```

### Layers

1. **API Layer** - REST endpoints
2. **Business Logic** - Views with filtering, searching, ordering
3. **Data Validation** - Serializers
4. **Data Persistence** - Models & PostgreSQL
5. **Performance** - Caching layer

---

## 🔧 Key Classes & Components

### 1. Ticket Model
```python
class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=100)
    category = models.CharField(max_length=50)
    priority = models.CharField(max_length=20)
```

**Fields**:
- `title` - Ticket subject (required)
- `description` - Detailed description
- `category` - Ticket category (e.g., technical, administrative)
- `priority` - Priority level (high, medium, low)

### 2. TicketSerializer
Handles data serialization/deserialization for Ticket model.

### 3. Views

#### `ticket_list(request)`
- **GET** - Retrieve all tickets with filtering, searching, ordering, pagination
- **POST** - Create new ticket
- **Cache** - 60-second cache for GET responses
- **Permissions** - Requires authentication

#### `ticket_detail(request, id)`
- **GET** - Retrieve specific ticket
- **PUT** - Full update
- **PATCH** - Partial update
- **DELETE** - Remove ticket
- **Cache** - 60-second cache
- **Error Handling** - 404 if ticket not found

### 4. Permissions
```python
class IsAdminOrReadOnly(BasePermission):
    # Only staff can modify, all can read
```

---

## 💾 Caching Strategy

### Redis Cache Configuration
```python
CACHE = {
    "DEFAULT": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}
```

### Caching Implementation
- **Cache Duration** - 60 seconds
- **Cache Key** - Auto-generated by Django based on view & params
- **Cache Invalidation** - Cleared on POST, PUT, PATCH, DELETE operations
- **Benefits** - Reduces database queries, improves response time

### Cache Usage in Views
```python
@cache_page(60)  # Cache for 60 seconds
def ticket_list(request):
    # ...

cache.clear()  # Clear on modifications
```

---

## 🐛 Troubleshooting

### 1. Database Connection Error
**Problem**: `psycopg2.OperationalError: could not connect to server`

**Solution**:
- Verify PostgreSQL is running
- Check database credentials in `settings.py`
- Ensure database exists: `createdb helpdesk_db`

### 2. Authentication Failed
**Problem**: `401 Unauthorized` or token issues

**Solution**:
- Obtain fresh token: `POST /api/token/`
- Verify token in Authorization header: `Bearer <token>`
- Check token expiration

### 3. Import Errors
**Problem**: `ModuleNotFoundError: No module named 'rest_framework'`

**Solution**:
```bash
pip install -r requirements.txt
# OR
pip install djangorestframework
```

### 4. Migration Issues
**Problem**: `django.db.utils.OperationalError: no such table`

**Solution**:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Permission Denied
**Problem**: `403 Forbidden`

**Solution**:
- Verify user has required permissions
- Check if superuser has IsAdminUser permission
- Review permission classes in settings

### 6. CORS Issues (Frontend Integration)
**Solution**: Add to `settings.py`:
```python
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React, Vue, etc.
]
```

---

## 📖 Common Management Commands

```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Django shell
python manage.py shell

# Clear cache
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()

# Collect static files (production)
python manage.py collectstatic
```

---

## 🤝 Contributing

1. **Create a feature branch**: `git checkout -b feature/your-feature`
2. **Make changes** and test locally
3. **Run tests**: `python manage.py test`
4. **Commit changes**: `git commit -m "Add feature description"`
5. **Push to branch**: `git push origin feature/your-feature`
6. **Create Pull Request** with detailed description

---

## 📄 License

This project is part of the PEP Python Course. All rights reserved.

---

## 📞 Support & Documentation

- **Django Docs**: https://docs.djangoproject.com/
- **DRF Docs**: https://www.django-rest-framework.org/
- **SimpleJWT Docs**: https://django-rest-framework-simplejwt.readthedocs.io/
- **PostgreSQL Docs**: https://www.postgresql.org/docs/

---

## 📝 Notes

- **Development Settings**: `DEBUG = True` (Change for production)
- **Secret Key**: Keep secure and use environment variables in production
- **Database**: PostgreSQL (configurable in `settings.py`)
- **Authentication**: JWT tokens with refresh capability
- **Default Page Size**: 2 tickets per page (configurable)
- **Cache TTL**: 60 seconds (adjustable in views)

---

**Last Updated**: February 2026
**Version**: 1.0.0
**Status**: Development

---

For more information or questions, refer to the individual file documentation and comments within the code.
