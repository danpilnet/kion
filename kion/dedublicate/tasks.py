from celery import shared_task
import hashlib
import json
import redis
from .models import Dublicate


r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)


@shared_task
def say_hello(user):
    json_ = json.dumps(user)
    string_ = hashlib.blake2s(json_.encode())
    if r.exists(f'user_id: {string_.hexdigest()}'):
        return 'Дубликат'

    if Dublicate.objects.filter(hash=string_.hexdigest()):
        return 'Дубликат'

    Dublicate.objects.create(hash=string_.hexdigest(), text=json_)

    r.hset(f'user_id: {string_.hexdigest()}', mapping=user)
    r.expire(f'user_id: {string_.hexdigest()}', 60)

    return 'Success'
