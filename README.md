# 🏡 Tourist Base Website — "Usadba na Chemalke"

**TourBaseWeb** is a production-ready web application developed for the tourist base **"Усадьба на Чемалке"**.  

![CI](https://img.shields.io/github/actions/workflow/status/radiant2958/TouristBaseSite/ci.yml?branch=main)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)


A Django-based web application for the tourist base **"Usadba na Chemalke"**.  
The website provides information about available rooms, services, news, and events,  
and allows users to submit booking requests online. It also includes Telegram bot integration  
to notify managers about new booking requests.

---
## 🌐 Production Website

The project is deployed and actively used by clients for real bookings.

- URL (Unicode): https://усадьбаначемалке.рф  

---

## ✨ Features
- **Room Booking System** — allows users to submit a room booking request online.
- **News & Events** — publish and manage updates about the tourist base.
- **Client Management** — store and manage customer data.
- **Telegram Bot Integration** — send automated notifications to managers when a booking request is received.
- **Responsive Design** — optimized for both desktop and mobile devices.

---

## 🛠 Tech Stack
- **Backend:** Django, Python
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)
- **Frontend:** HTML, CSS, JS (Django templates)
- **Testing:** pytest, pytest-django, pytest-asyncio, aioresponses
- **Code Quality:** black, isort, flake8 (with pre-commit hooks)
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions

---

## 📂 Project Structure
```
TourBaseWeb/
├── base/ # Main application logic
│ ├── bookings/ # Booking-related views, forms, and models
│ ├── clients/ # Client management
│ ├── news/ # News and events
│ ├── telegram_bot/ # Telegram bot integration
│ ├── templates/ # HTML templates
│ ├── tests/ # Automated tests
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── base_backend/ # Project settings and configuration
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
├── static/ # Static files (CSS, JS, images)
├── .github/workflows/ # CI/CD configuration
├── .env.example # Environment variables example
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── pytest.ini
├── requirements.txt
├── .pre-commit-config.yaml
├── .flake8
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository
```
git clone https://github.com/radiant2958/TouristBaseSite.git
cd TouristBaseSite
```

### 2. Create and activate a virtual environment
```
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Create .env file
```
Copy .env.example to .env and set your environment variables.
```

### 5. Run migrations
```
python manage.py migrate
```

### 6. Run the development server
```
python manage.py runserver
```

##🧪 Running Tests
```
pytest
```

Tests are automatically run on every push via GitHub Actions.

## 📦 Using Docker
```
docker-compose up --build
```

