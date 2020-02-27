from django.db import models
from django.conf import settings
# Create your models here.

class History(models.Model):
    expression = models.TextField(default='')
    answer = models.TextField(default='')
    