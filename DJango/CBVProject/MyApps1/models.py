from django.db import models


# Create your models here.
# ListView
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.FloatField()
