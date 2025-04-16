import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kion.settings")
app = Celery("kion")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
