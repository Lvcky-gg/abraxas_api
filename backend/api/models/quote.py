from django.db import models
from django.contrib.auth.models import User
from .person import Person

class Quote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quoted_by_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.TextField(max_length=200, unique=True)
    body = models.TextField(max_length=1000, unique=True)
    date_quoted = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)