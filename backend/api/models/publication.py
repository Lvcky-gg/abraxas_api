from django.db import models
from django.contrib.auth.models import User
from .person import Person
from .quote import Quote


class Publication(models.Model):
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE)
    added_by_id = models.ForeignKey(User, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)