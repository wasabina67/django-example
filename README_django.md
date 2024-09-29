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
