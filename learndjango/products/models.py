from django.db import models

# Create your models here.
class Product(models.Model): 
    title   = models.TextField()
    price   = models.TextField()
    summary = models.TextField()
    description = models.TextField(default='yoo')