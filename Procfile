web: gunicorn TestPro.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
manage.py migrate authtoken