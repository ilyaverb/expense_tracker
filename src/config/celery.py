from django.conf import settings

from celery import Celery
from celery.schedules import crontab


app = Celery('Expense accounting manager')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-statistics-every-day-at-8-am': {
        'task': 'api.core.tasks.send_statistics',
        'schedule': crontab(hour=8, minute=0)
    }
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
