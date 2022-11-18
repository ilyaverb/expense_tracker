import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

app = Celery('expense_tracker')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-statistics-every-1-minute': {
        'task': 'expense_tracker.core.tasks.send_statistics',
        'schedule': crontab(minute='*/1'),
    },
}
