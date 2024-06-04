from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=2, decimal_places=2)
    image = models.ImageField(upload_to="imagens/")

class Cart(models.Model):
    user = models.ForeignKey
    created_at = models.DateTimeField

class CartItem(models.Model):
    cart = models.ForeignKey
    product = models.ForeignKey
    quantity = models.IntegerField