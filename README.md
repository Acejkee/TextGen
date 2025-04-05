✏️ TextGen

TextGen - это сервис генерации текста на основе ИИ, построенный с использованием Django, Django REST Framework, Celery и OpenAI. Он предоставляет API для создания запросов на генерацию текста, асинхронной обработки этих запросов с помощью Celery и Redis, и отправки результатов по электронной почте через Mailersend.

Технологический стек:

- **Python 3.11+**
- **Django 5.x**
- **Django REST Framework (DRF)**
- **PostgreSQL**
- **Celery**
- **Redis**
- **OpenAI**
- **Docker, Docker Compose**
- **Mailersend**

Быстрый старт:

1. Клонируйте репозиторий:
```bash
   git clone https://github.com/Acejkee/TextGen.git
```
2. Перейдите в директорию проекта:
```bash
    cd TextGen
```

3.  Создайте файл `.env` на основе `.env.example` и заполните необходимые переменные (секретный ключ Django, данные для подключения к БД, OpenAI API Key, SMTP данные).


4.  Запустите проект с помощью Docker Compose: 
```bash
  docker-compose up --build
```

5.  API будет доступно по адресу `http://localhost:8000/api/`

