﻿
# User Management API with Admin Capabilities

This project is a Django-based User Management API with role-based access control, JWT authentication, and admin-specific functionalities. It also includes interactive API documentation using Swagger.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Generating Authentication Tokens](#generating-authentication-tokens)
- [Creating the Initial Admin User](#creating-the-initial-admin-user)
- [Accessing API Documentation](#accessing-api-documentation)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)

## Features
- JWT Authentication for secure API access.
- Role-based access control with "user" and "admin" roles.
- Admin-specific endpoints for managing users.
- Swagger-based API documentation.
- Custom Django management command to create an initial admin user.

## Prerequisites
- Python 3.8+
- Django 4.0+
- Virtualenv (recommended)

## Installation

1. *Clone the repository:*

   ```bash
   git clone https://github.com/Varun11Kumar/myproject.git
   cd myproject
Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Apply the database migrations:

python manage.py migrate
Running the Application

Start the Django development server:

python manage.py runserver
The application will be available at http://127.0.0.1:8000/.

Generating Authentication Tokens
To authenticate a user and receive a JWT token:

Register a new user:

POST /api/register/
Example payload:

{
    "username": "newuser",
    "password": "newpassword",
    "email": "newuser@example.com"
}
Login the user:

POST /api/login/
Example payload:

{
    "username": "newuser",
    "password": "newpassword"
}
The response will include a JWT token:

{
    "refresh": "refresh_token",
    "access": "access_token"
}
Include the token in the Authorization header for protected endpoints:

Authorization: Bearer access_token
Creating the Initial Admin User
Use the custom Django management command create_admin to create an initial admin user:

python manage.py create_admin
The command will create an admin user with the following credentials:

Username: admin
Email: admin@example.com
Password: adminpassword
You can log in with these credentials and obtain an admin JWT token for accessing admin-specific endpoints.

Accessing API Documentation
Swagger-based API documentation is automatically generated and can be accessed at:

http://127.0.0.1:8000/swagger/
Use the documentation to explore and test the API endpoints interactively.

Project Structure
yourproject/
├── accounts/
│   ├── management/
│   │   └── commands/
│   │       └── create_admin.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── ...
├── yourproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md


Troubleshooting
Common Issues:
Command not found: Ensure the directory structure is correct, and the app is included in INSTALLED_APPS in settings.py.
Token errors: Verify that the token is valid and included in the request headers.
For any other issues, please consult the Django and DRF documentation or raise an issue in the repository.
