# channels
This is intended to be an example code in case someone needs an example of; web sockets, django-channels and celery to have a task run.

Requires; redis/rabbitmq, asgi_redis, django-channels & celery

Commands

1) redis-server
2) python manage.py runworker
3) python manage.py runserver --noworker
4) celery worker --app ch.celery_app --autoscale=10,3

On clicking button a "process" starts in background and streams the data back to the front end.
