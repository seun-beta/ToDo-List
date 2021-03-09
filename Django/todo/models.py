from django.db import models
from django.core.validators import MinLengthValidator

class Task(models.Model):
    task = models.CharField(
        max_length=200,
        help_text='Enter a task',
        validators = [MinLengthValidator(1, "Task must be greater than 1 character")]
    )
    description = models.CharField(
        max_length=500,
        help_text= "Enter the description of your task"  
    )

    def __str__(self):
        return self.task
