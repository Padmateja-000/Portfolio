# Django Portfolio Website Setup

This is a modern, responsive, and production-ready portfolio website built with:
- **Django** (Backend & Admin)
- **Tailwind CSS** (Frontend Styling & Responsive Design)
- **AOS.js** (Scroll Animations)
- **Vanilla JS & CSS 3D Transforms** (Interactive elements like 3D Tilt Cards)

## Project Architecture

```text
Portfolio/
├── manage.py                # Django entry point
├── requirements.txt         # Project dependencies (Django, Pillow)
├── config/                  # Core Django Settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── portfolio/               # Main App containing all portfolio logic
    ├── admin.py             # Admin Dashboard configuration
    ├── models.py            # Database Models (Skills, Projects, etc.)
    ├── views.py             # View logic and Contact form handling
    ├── urls.py              # Routing for the app
    ├── templates/
    │   ├── base.html        # Global Layout, Navbar, Footer
    │   └── portfolio/
    │       └── index.html   # Main Landing Page content
    └── static/
        ├── css/
        │   └── style.css    # Custom styling, animations, scrollbars
        └── js/
            └── main.js      # Intersection observers, AOS init, 3D tilts
```

## How to Run

1. **Install Python**
   If Python is not installed, download it from [python.org](https://www.python.org/downloads/) or the Microsoft Store.

2. **Open Terminal**
   Navigate to the `Portfolio` folder.

3. **Set up Virtual Environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # For Windows
   # source venv/bin/activate # For Mac/Linux
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create an Admin User (Superuser)**
   ```bash
   python manage.py createsuperuser
   ```
   *Follow the prompts to set a username, email, and password.*

7. **Run the Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Website**
   - Frontend: Go to `http://127.0.0.1:8000/`
   - Admin Panel: Go to `http://127.0.0.1:8000/admin/` and log in to add Skills, Projects, Education, etc.

## Features

- **Dynamic Content**: All sections (Skills, Projects, Education, Training, Certificates, Achievements) are driven by the database.
- **Modern UI**: Dark theme by default with vibrant blue/purple accents.
- **Interactive 3D Cards**: Project cards tilt dynamically based on mouse position.
- **Scroll Animations**: Elements fade, zoom, and slide in as you scroll using AOS.
- **Working Contact Form**: Sends messages directly to the Django database for you to view in the admin panel.
- **Responsive Navigation**: Mobile-friendly hamburger menu.
