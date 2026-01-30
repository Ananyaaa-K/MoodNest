# MoodNest 🌿
**Mood-Based Mini Habit Generator**

MoodNest is a minimalist, Django-based web application designed to help you take small, meaningful steps forward based on your current emotional state. Instead of overwhelming to-do lists, MoodNest suggests **micro-habits** tailored to how you feel right now.

## 🌟 Features

*   **Mood Selection**: Choose from 6 core moods (Tired, Anxious, Stressed, Lazy, Sad, Neutral).
*   **Smart Suggestions**: Get instant, actionable micro-habits (1-5 mins) mapped to your mood.
*   **Daily Streak 🔥**: Track your consistency with a daily streak counter.
*   **User Profile 👤**: Manage your personal details.
*   **Shuffle 🔀**: Don't like a suggestion? Shuffle to get a different one without duplicates.
*   **Quote of the Day 💬**: Daily dose of inspiration on your home screen.
*   **History**: View your past moods and habits to spot patterns.
*   **Minimalist UI**: calm, beautiful interface with dark mode support.

## 📚 Documentation
- [**Architecture**](ARCHITECTURE.md): System design and data flow.
- [**Setup Guide**](SETUP.md): Detailed instructions for local development.
- [**Contributing**](CONTRIBUTING.md): How to get involved.

## 🛠️ Tech Stack

*   **Backend**: Python 3, Django 5
*   **Frontend**: HTML5, Tailwind CSS (via CDN)
*   **Database**: SQLite (default)
*   **Styling**: Custom CSS variables for clean design, responsive layout.

## 🚀 Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ananyaaa-K/MoodNest.git
    cd MoodNest
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If requirements.txt is missing, install Django directly: `pip install django`)*

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```
    *(Optional: Run `python manage.py seed_habits` if you have the command, otherwise create habits via Admin)*

5.  **Create a Superuser (to add habits):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the App:**
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## 📸 Usage

1.  **Sign Up/Login**: Create an account to track streaks and history.
2.  **Select Mood**: Click the button that matches your current feeling.
3.  **Do the Habit**: Complete the small task suggesting.
4.  **Click "I Did It"**: Celebrate the small win!

---
*Built with 💙 for mental wellness.*