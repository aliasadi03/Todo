from django.db import models

# Create your models here.

class User:
    username = models.CharField()
    email = models.EmailField()
    password = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_created=True)
