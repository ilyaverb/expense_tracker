import os

from django.conf import settings

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

app = Celery('config')

app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')


app.conf.beat_schedule = {
    'send-statistics-every-day': {
        'task': 'expense_tracker.core.tasks.send_statistics',
        'schedule': crontab(hour=0, minute=0),
    },
}

app.autodiscover_tasks()
