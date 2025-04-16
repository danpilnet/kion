from celery import shared_task
import hashlib

@shared_task
def say_hello(request):
    print(request)