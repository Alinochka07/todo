from django.db import models
from django_prices.models import MoneyField


class Todo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class Price(models.Model):
    currency = models.CharField(max_length=3, default="KGS")
    cost_amount = models.CharField(max_length=100)
    