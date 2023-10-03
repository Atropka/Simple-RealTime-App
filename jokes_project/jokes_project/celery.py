import os
from celery import  Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jokes_project.settings')

app = Celery('jokes_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_number_5s':{
        'task': 'jokes.tasks.get_number',
        'schedule': 5.0
    }
}

app.autodiscover_tasks()