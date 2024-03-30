## Installation

### 1. Install Python

If Python is not already installed on your system, you can download and install it from the official website: [Python Downloads](https://www.python.org/downloads/)

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies for Python projects. Open a terminal and run the following commands to create and activate a virtual environment:

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# For Windows
myenv\Scripts\activate
# For macOS/Linux
source myenv/bin/activate
```

### 3. Install Django

With the virtual environment activated, install Django using pip:

```bash
pip install django
```

## Basic Commands

### Initializing a Django Project

To initialize a new Django project, run the following command:

```bash
django-admin startproject InventoryMgtSystem
```

## Creating Django App

Navigate into the project directory and create a new Django app:

```bash
cd InventoryMgtSystem
django-admin startapp InventoryMgtSystem
```

## Running Migrations

Django uses migrations to manage database schema changes. Run the following commands to apply migrations:

### Navigate to the project directory

```bash
cd InventoryMgtSystem
```

### Run migrations

```bash
python manage.py migrate
```

## Running the Application

To run the Django development server and access the ToDo app, execute the following command:

```bash
python manage.py runserver
```