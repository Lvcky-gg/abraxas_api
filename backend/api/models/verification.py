from django.db import models
from django.contrib.auth.models import User
from .quote import Quote

class Verification(models.Model):
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)