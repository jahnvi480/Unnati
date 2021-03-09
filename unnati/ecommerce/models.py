from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/shop",default="")

    def __str__(self):
        return self.product_name

class CartQty(models.Model):
    users = models.CharField(max_length=50,default="")
    Aachar  = models.IntegerField(default=0)
    Papad = models.IntegerField(default=0)
    P_C = models.IntegerField(default=0)
    K_M_G = models.IntegerField(default=0)
    Lemonade  = models.IntegerField(default=0)

    def __str__(self):
        return str(self.users)


class Cart(models.Model):
    users = models.CharField(max_length=50,default="")
    products = models.ManyToManyField(Product)
    total = models.IntegerField(default=0)
    qty = models.ManyToManyField(CartQty)
    def __str__(self):
        return str(self.users)

class Address(models.Model):
    users = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    pin_code = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=10,default="")
    def __str__(self):
        return str(self.users)