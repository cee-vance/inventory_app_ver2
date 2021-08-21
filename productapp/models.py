from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
import productapp.models


class ProductCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length = 50)
    #slug = models.SlugField()

    def __str__(self):

        return self.name

class Product(models.Model):
    """
    This class represents a product
    with name, description, and
    price
    """
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField(default=10000)

    image = models.ImageField(upload_to='images/', blank=True)

    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, default=None, null=True)

    create_date = models.DateField(default=date.today)

    product_category = models.ManyToManyField(ProductCategory, blank=True)




    def __str__(self):
        return self.name



