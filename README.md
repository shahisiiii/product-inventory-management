# Product Inventory Management System

## Backend

Django REST Framework backend with JWT authentication, role-based access control, and Redis caching.


## Features

Custom User Model with role-based access (ADMIN/CUSTOMER)

JWT Authentication (access + refresh tokens)

Role-Based Permissions (Admin: full access, Customer: read-only)

Redis Caching for improved performance

PostgreSQL/SQLite database support

PEP8 Compliant with pre-commit hooks

## Tech Stack

Python 3.11+

Django 4.2

Django REST Framework

PostgreSQL

Redis

JWT Authentication

## Setup Instructions

### 1. Clone Repository

```bash
    git clone <repository-url>

    cd backend
```

### 2. Create Virtual Environment

```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
    pip install -r requirements.txt
```
### 4. Environment Configuration
```bash
    cp .env.example .env
```

Edit .env with your configuration

### 5. Database Setup
```bash
    python manage.py makemigrations

    python manage.py migrate
```
### 6. Create Superuser
```bash
    python manage.py createsuperuser
```

### 7. Install Pre-commit Hooks
``` bash
    pre-commit install
```

### Edit .env file:
```
SECRET_KEY=your-very-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

 For PostgreSQL (Production)
 DB_ENGINE=django.db.backends.postgresql
 DB_NAME=inventory_db
 DB_USER=postgres
 DB_PASSWORD=your_password
 DB_HOST=localhost
 DB_PORT=5432

REDIS_URL=redis://127.0.0.1:6379/1
CORS_ALLOWED_ORIGINS=http://localhost:3000
## API Endpoints
```
###  Install and Start Redis

Verify Redis is running:

```bash
redis-cli ping
```

## Create Admin Users

### Create superuser (Admin)

```python manage.py createsuperuser```

#Email: admin@example.com
#Username: admin
#Password: admin123

### Create test customer (via Django shell)

```python manage.py shell```

### In shell:

### create a customer user
```bash
from apps.accounts.models import User
customer = User.objects.create_user(
    username='customer',
    email='customer@example.com',
    password='customer123',
    role='CUSTOMER'
)
```

### create a Admin user
```bash
from apps.accounts.models import User
customer = User.objects.create_user(
    username='admin',
    email='admin@example.com',
    password='admin123',
    role='ADMIN'
)
```

### Run Development Server
```bash
    python manage.py runserver
```


### Authentication

``` POST /api/auth/login/ - Login and get tokens ```

```POST /api/auth/logout/ - Logout (blacklist token)```

```POST /api/auth/refresh/ - Refresh access token```

```GET /api/auth/me/ - Get current user info ```

### Products

```GET /api/products/ - List all products (Admin & Customer)```

```GET /api/products/{id}/ - Get product details (Admin & Customer)```

```POST /api/products/ - Create product (Admin only)```

```PUT /api/products/{id}/ - Update product (Admin only)```

```PATCH /api/products/{id}/ - Partial update (Admin only)```

```DELETE /api/products/{id}/ - Delete product (Admin only)```

### User Roles
```ADMIN```

Full CRUD access to products

Can create, update, delete products

```CUSTOMER```

Read-only access
Can view product list and details

### Caching Strategy

Product List: Cached for 5 minutes

Product Detail: Cached for 5 minutes

Cache Invalidation: Automatic on create/update/delete


### Code Quality

```Run Black (Code Formatter)```

```bashblack```

```Run Flake8 (Linter)```

```bashflake8```

```Pre-commit Checks```

```bashpre-commit run --all-files```

## Project Structure

```
backend/
├──apps
├    ├── accounts/              # User authentication
│    │   ├── models.py         # Custom User model
│    │   ├── serializers.py    # Auth serializers
│    │   └── views.py          # Auth views
├    ├── products/             # Product management
│    │   ├── models.py         # Product model
│    │   ├── serializers.py    # Product serializers
│    │   ├── views.py          # Product views with caching
│    │   └── permissions.py    # Custom permissions
├── inventory_system/     # Main project
│   ├── settings.py       # Django settings
│   └── urls.py           # URL configuration
├── requirements.txt      # Dependencies
├── .env.example          # Environment variables template
└── manage.py             # Django management script
```


# Product Inventory Management System - Frontend

React.js frontend with JWT authentication, role-based UI, and real-time product management.

### Features

JWT Authentication with automatic token refresh

Role-Based UI (Admin vs Customer views)

Product Management (CRUD operations for Admin)

Responsive Design with modern CSS

Error Handling with user-friendly messages

## Setup Instructions
### 1. Prerequisites

Node.js 16+ and npm

Backend API running on http://localhost:8000

### 2. Install Dependencies

```bash
cd frontend
```

```bash
npm install
```


### 3. Environment Setup

The app is configured to connect to backend at http://localhost:8000. To change this, update the baseURL in src/api/axios.js.

### 4. Run Development Server
```bash
npm start
```

App will open at http://localhost:3000


### 5. Build for Production
```bash
npm run build
```

## Project Structure

```
src/
├── api/
│   └── axios.js           # Axios configuration with interceptors
├── components/
│   ├── Login.js           # Login page
│   ├── Login.css
│   ├── Navbar.js          # Navigation bar
│   ├── Navbar.css
│   ├── ProductList.js     # Product list view
│   ├── ProductList.css
│   ├── ProductForm.js     # Add/Edit product form
│   └── ProductForm.css
├── context/
│   └── AuthContext.js     # Authentication context
├── App.js                 # Main app component
├── App.css               # Global styles
└── index.js              # Entry point
```

## Features by Role

### Admin Users

View all products

Add new products

Edit existing products

Delete products

### Customer Users

View product list

View product details

Read-only access

## API Integration

### Authentication Flow

User logs in with email/password

Backend returns access + refresh tokens

Access token stored in localStorage

Axios automatically attaches token to requests

On 401 error, automatically refreshes token

On refresh failure, redirects to login


### Protected Routes
All routes except /login require authentication. Unauthenticated users are redirected to login page.

Key Components

AuthContext

## Manages authentication state across the app:

Login/Logout functions

Current user data

Role checking helpers (isAdmin, isCustomer)

### Axios Interceptors

Request Interceptor: Adds JWT token to all requests

Response Interceptor: Handles token refresh on 401 errors

### Product Management

ProductList: Displays products with conditional admin actions

ProductForm: Modal form for creating/editing products

### Styling

Uses vanilla CSS with:

Modern card-based layouts

Gradient backgrounds

Smooth transitions

Responsive grid system

Mobile-friendly design

### Error Handling

API errors shown with user-friendly messages

Network errors handled gracefully

Token expiry triggers automatic logout

Validation errors displayed in forms
