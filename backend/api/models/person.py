from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    added_by_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

