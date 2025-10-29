# Лабораторная работа №2 — Django «Создание web-страницы с текстом»

Проект создан строго по методическим указаниям. В комплекте:
- Django-проект `firstwebpage`
- Приложение `flatpages` (кастомное, не `django.contrib.flatpages`)
- Шаблоны: `templates/index.html` и `templates/static_handler.html`
- Статические файлы: `static/index.css` и `logo.png`
- Команда для создания суперпользователя `rsb` — `python manage.py createsu`
- `requirements.txt` с `Django==2.1.7`

## Быстрый старт

```bash
cd firstwebpage
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt

# Создать таблицы БД (см. ЛР1)
python manage.py migrate

# Создать суперпользователя rsb/12345678
python manage.py createsu

# Запуск сервера
python manage.py runserver
```

Откройте:
- Главная: http://127.0.0.1:8000/  (шаблон `templates/index.html`)
- Тот же текст по адресу /hello/: http://127.0.0.1:8000/hello/
- Админка: http://127.0.0.1:8000/admin/  (логин `rsb`, пароль `12345678`)

> Примечание по CSS-ссылке: в `static_handler.html` ссылка на стили оформлена **в точности как в методичке** — `{ STATIC_URL }/static/index.css`. 
> Для совместимости также добавлен файл по пути `/static/static/index.css`.
