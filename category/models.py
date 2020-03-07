from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
