# deep_research_system/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deep_research_system.settings')

app = Celery('deep_research_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
