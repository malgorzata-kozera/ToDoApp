from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):

    task = models.CharField(max_length=300)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
