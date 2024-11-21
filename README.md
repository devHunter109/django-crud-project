# Expense Tracker API

This project is a Django-based Expense Tracker API that allows users to track their expenses. The API provides CRUD operations for managing users and expenses, as well as additional endpoints for listing expenses by date range and summarizing expenses by category.

## Project Setup

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Apply migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Create a superuser to access the Django admin:
    ```sh
    python manage.py createsuperuser
    ```

4. Load initial data (optional for testing):
    ```sh
    python manage.py loaddata initial_users.json
    python manage.py loaddata initial_expenses.json
    ```

5. Run the server:
    ```sh
    python manage.py runserver
    ```

## Available API Endpoints

### User Endpoints

- **List all users**:
    - `GET /users/`
    - Response: List of all user objects

- **Create a new user**:
    - `POST /users/`
    - Request Body: JSON object containing `username` and `email`
    - Response: Created user object

- **Retrieve a user**:
    - `GET /users/<id>/`
    - Response: User object with specified ID

- **Update a user**:
    - `PUT /users/<id>/`
    - Request Body: JSON object containing `username` and/or `email`
    - Response: Updated user object

- **Delete a user**:
    - `DELETE /users/<id>/`
    - Response: Status message

### Expense Endpoints

- **List all expenses**:
    - `GET /expenses/`
    - Response: List of all expense objects

- **Create a new expense**:
    - `POST /expenses/`
    - Request Body: JSON object containing `user`, `title`, `amount`, `date`, and `category`
    - Response: Created expense object

- **Retrieve an expense**:
    - `GET /expenses/<id>/`
    - Response: Expense object with specified ID

- **Update an expense**:
    - `PUT /expenses/<id>/`
    - Request Body: JSON object containing `user`, `title`, `amount`, `date`, and/or `category`
    - Response: Updated expense object

- **Delete an expense**:
    - `DELETE /expenses/<id>/`
    - Response: Status message

- **List expenses by date range**:
    - `GET /expenses/user/<user_id>/range/<start_date>/<end_date>/`
    - Response: List of expense objects for the user within the specified date range

- **Category summary for a month**:
    - `GET /expenses/user/<user_id>/summary/<year>/<month>/`
    - Response: Total expenses per category for the user in the specified month
