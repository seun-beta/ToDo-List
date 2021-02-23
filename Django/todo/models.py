from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=256)
    task_description = models.CharField(max_length=400)
