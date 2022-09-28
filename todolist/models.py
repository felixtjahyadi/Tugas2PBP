from email.policy import default
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_finished = models.BooleanField(default = False)