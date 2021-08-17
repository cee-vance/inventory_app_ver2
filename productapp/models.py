from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
import productapp.models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length = 50)
    slug = models.SlugField()

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

    #image = models.ImageField(upload_to='images/', blank=True)

    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    create_date = models.DateField(default=date.today)

    #category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # toString
    def __str__(self):
        return self.name


