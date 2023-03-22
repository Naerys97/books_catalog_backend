
#!/bin/sh
python3 manage.py collectstatic --noinput
python3 manage.py migrate
gunicorn myproject.wsgi --workers 3 --bind 0.0.0.0:8000 --log-level info