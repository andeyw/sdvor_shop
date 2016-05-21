import string
from macpath import join

from Crypto.Random import random
from django.db import models

# Create your models here.

class Category(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=250)
    def get_quantity(self):
        return len(Product.objects.filter(category=self))
class Product(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()





