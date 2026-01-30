# Development Setup Guide 🛠️

This guide will help you set up a local development environment for MoodNest.

## Prerequisites

- **Python 3.10+**: Ensure Python is installed and added to your PATH.
- **Git**: For version control.
- **Virtualenv**: Recommended to isolate dependencies.

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ananyaaa-K/MoodNest.git
cd MoodNest
```

### 2. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
*If `requirements.txt` is missing, install the core dependencies:*
```bash
pip install django pytest pytest-django
```

### 4. Database Setup

Run the migrations to create the SQLite database:
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)

You'll need an admin account to manage habits:
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### 6. Run the Development Server

```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser.

## Running Tests

We use `pytest` for testing. To run the full test suite:

```bash
pytest
```

## Common Issues

- **Static Files Not Loading**: Ensure `DEBUG = True` in `settings.py`.
- **Database Locked**: If using SQLite, ensure no other process (like a DB viewer) has the file open.
