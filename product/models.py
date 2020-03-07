from django.db import models
import datetime

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()
    cat_id = models.IntegerField() 
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)