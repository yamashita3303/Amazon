from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    
class Text(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    detail = models.CharField(max_length=1000)

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
 
    def total_price(self):
        return self.item.price * self.quantity
 
    def __str__(self):
        return f"{self.user.username}：{self.item.title} × {self.quantity}個購入"
    
"""
class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=8)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}：{self.code} ※{self.address}"
"""