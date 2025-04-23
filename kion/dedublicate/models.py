from django.db import models


class Dublicate(models.Model):
    hash = models.CharField(unique=True)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)