from django.db import models
from django.contrib.auth.models import User
from .quote import Quote

class Region(models.Model):
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)