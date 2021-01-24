from django.db import models
import datetime




class Todo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class BookShop(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    books_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True)
    is_favorites = models.BooleanField(default=False)


    
    
    