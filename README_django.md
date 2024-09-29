# Django コマンドリファレンス

## Install

```bash
pip install django
```

## Start

```bash
django-admin startproject prj .
```

```bash
python manage.py startapp myapp
```

## Update INSTALLED_APPS in prj/settings.py

```python
INSTALLED_APPS = [
    ...
    'myapp',
]

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
```

- Update myapp/models.py

## Migration

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### One liner

```bash
python manage.py makemigrations && python manage.py migrate
```

## Update myapp/admin.py

```python
from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
```

## Createsuperuser

```bash
python manage.py createsuperuser
```

### user1

```bash
user1
```

```bash
user1@example.com
```

```bash
password6767
```

### user2

```bash
user2
```

```bash
password6767
```

## Runserver

```bash
python manage.py runserver
```

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/login/
