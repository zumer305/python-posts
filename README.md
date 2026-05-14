# Python Posts - Django REST API

A Django REST Framework application for managing user accounts and creating/updating posts with JWT authentication.

## Project Structure

```
python-posts/
├── core/                    # Django project settings
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/                # User management app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
└── posts/                   # Posts management app
    ├── models.py
    ├── views.py
    ├── urls.py
    └── migrations/
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Install dependencies:**

   ```bash
   pip install django
   pip install djangorestframework
   pip install djangorestframework-simplejwt
   ```

2. **Configure Django settings:**

   Add the following to `core/settings.py`:

   ```python
   INSTALLED_APPS = [
       'rest_framework',
       'accounts',
       'posts',
   ]

   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       )
   }
   ```

3. **Run migrations:**

   ```bash
   cd core
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- **Sign Up:** `POST /api/accounts/signup/`
  - Register a new user
  - Example: `http://127.0.0.1:8000/api/accounts/signup/`

- **Get Token:** `POST /api/token/`
  - Obtain JWT access token
  - Example: `http://127.0.0.1:8000/api/token/`
  - Credentials:
    ```json
    {
      "username": "ali",
      "password": "123"
    }
    ```

### Posts Management

- **Create Post:** `POST /api/posts/create/`
  - Create a new post (requires authentication)
  - Example: `http://127.0.0.1:8000/api/posts/create/`

- **Update Post:** `POST /api/posts/update/<id>/`
  - Update an existing post
  - Example: `http://127.0.0.1:8000/api/posts/update/1/`

## Usage Example

### 1. Sign Up

```bash
POST /api/accounts/signup/
```

### 2. Get Access Token

```bash
POST /api/token/
Body: {
  "username": "ali",
  "password": "123"
}
```

### 3. Create a Post

```bash
POST /api/posts/create/
Headers: Authorization: Bearer <access_token>
```

### 4. Update a Post

```bash
POST /api/posts/update/1/
Headers: Authorization: Bearer <access_token>
```

## Features

- User authentication with JWT tokens
- User signup functionality
- Create and manage posts
- Token-based authorization for protected endpoints

## Database

The project uses SQLite by default. The database file is located at `core/db.sqlite3`.

## Additional Notes

- All protected endpoints require a valid JWT access token in the Authorization header
- Format: `Authorization: Bearer <access_token>`
- Tokens are obtained via the `/api/token/` endpoint after user signup
