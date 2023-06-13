from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)