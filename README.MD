ссTourBaseWeb
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


Установка и запуск
Для установки и локального запуска проекта выполните следующие шаги:

Клонирование репозитория:

bash
Copy code
git clone <URL репозитория>
cd TourBaseWeb

Создание виртуального окружения и установка зависимостей:

bash
Copy code
python -m venv venv
source venv/bin/activate  # Используйте venv\Scripts\activate на Windows
pip install -r requirements.txt
Настройка переменных окружения:

Создайте файл .env на основе предоставленного шаблона и заполните его соответствующими значениями.
Выполнение миграций:

Copy code
python manage.py migrate
Запуск сервера разработки:

Copy code
python manage.py runserver
Открытие веб-приложения в браузере:

Перейдите по адресу http://127.0.0.1:8000 в вашем браузере.


Тестирование
Выполните тесты, используя команду:

Copy code
pytest
