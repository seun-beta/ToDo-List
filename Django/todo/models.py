from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=256)
    task_description = models.CharField(max_length=400)

    #def __str__(self):
    #    return self.task, self.task_description