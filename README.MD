TourBaseWeb
TourBaseWeb — это веб-приложение на Django, предназначенное для управления и организации туристических услуг. 
Проект включает в себя функционал для бронирования, управления клиентской информацией и интеграции с Telegram для уведомлений о заявки на бронирование.


* Структура проекта *

TourBaseWeb/
├── base/

│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   └── base/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── base_backend/

│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/

│   ├── admin/
│   ├── css/
│   ├── fonts/
│   ├── images/
│   ├── img/
│   └── js/
├── .gitignore
├── manage.py
├── pytest.ini
├── README.md
└── requirements.txt


base/: Основное Django приложение.
__pycache__/: Содержит скомпилированные байт-коды Python для ускорения загрузки.
migrations/: Миграции базы данных.
templates/: HTML шаблоны для приложения.
admin.py, apps.py, forms.py, models.py, tests.py, urls.py, views.py: Основные файлы приложения, включая настройки административной панели, формы, модели, тесты, маршруты URL и представления.
base_backend/: Настройки проекта Django.
asgi.py, settings.py, urls.py, wsgi.py: Конфигурационные файлы для ASGI и WSGI, настройки проекта и маршруты URL.
static/: Статические файлы (CSS, JavaScript, изображения).
.gitignore: Список исключений для Git.
manage.py: Утилита для управления Django проектом.
pytest.ini: Конфигурация для pytest.
requirements.txt: Список зависимостей Python.

