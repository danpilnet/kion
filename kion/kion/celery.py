import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kion.settings")
app = Celery("kion")
app.config_from_project("django.conf:settings", namespace="CELERY")
app.autodiscover_task()
