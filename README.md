ASKmi... is a Quora-inspired Question & Answer web application built with Django. It allows users to register, log in, ask questions, answer others' questions, like helpful answers, and manage their profile.
The platform is designed for learning and practicing Django fundamentals like user authentication, form handling, class-based and function-based views, template rendering, and CRUD operations.
This project is ideal for beginners who want to build a full-stack Django app and understand how dynamic content, user interaction, and data models work together in a real-world scenario.

 *Features
🔐 User Authentication (Login, Register, Logout)
❓ Post & View Questions
💬 Answer Questions
👍 Like Answers
✏️ Edit/Delete your Questions & Answers
🔍 Search Questions
👤 Profile Page
🏠 Home Page with Navbar
Forgot Password via Email (Password Reset)
Unique Username & Email Validation

*Tech used
Backend: Django 4.x (Python)
Frontend: HTML, CSS (Bootstrap 5)
Database: SQLite (Default)
Authentication: Django’s built-in auth system
Email: Console backend for development


*Project Structure
askmi_project/
│
├── portal/                # Main app
│   ├── templates/         # All HTML templates
│   ├── views.py           # Core logic
│   ├── models.py          # Database models
│   ├── forms.py           # Django forms
│   ├── urls.py            # App URL routing
│
├── askmi_project/         # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3             # Default database
├── manage.py              # Django entry point
└── README.md              # This file


*Run Migrations & Start Server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

*Access the App
Open your browser and visit:
http://127.0.0.1:8000/

*screenshots of the homepage, ask-question, answers, login/register pages here for better visibility on GitHub.
![Screenshot 2025-04-10 194151](https://github.com/user-attachments/assets/fa6b6667-cd5f-45bf-bb53-1d24c3048cc2)

![Screenshot 2025-04-10 194134](https://github.com/user-attachments/assets/fe1190e7-771d-40ec-b9a6-78b68866b21e)

![Screenshot 2025-04-10 194217](https://github.com/user-attachments/assets/f2eacdda-3da5-4beb-9682-778fa9db4f1b)

