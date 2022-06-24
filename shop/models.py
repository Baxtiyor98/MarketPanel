from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Volume(models.Model):
    category = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    vol = models.ForeignKey(Volume,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Products',null=True,blank=True)
    price = models.FloatField()
    discount = models.IntegerField(default=0)

    shtrix_code = models.CharField(max_length=20)


    @property
    def price_with_discount(self):
        return self.price * (1 - self.discount / 100)


    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name



class Casher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    required_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Sale(models.Model):
    pay_type = {
        ('Naqd', 'Naqd'),
        ('UzCard', 'UzCard'),
        ('Humo', 'Humo'),
        ('PaymeGo', 'PaymeGo'),
        ('Click', 'Click')
    }
    seller = models.ForeignKey(Casher, on_delete=models.SET_NULL, null=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    payment = models.CharField(max_length=10, choices=pay_type, null=True,blank=True)

    def __str__(self):
        return f"{self.id}"

class Card(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products,on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField(default=1)
    sale_edited_date = models.DateTimeField(auto_now_add=True)
    sold_price = models.FloatField(default=0, null=True, blank=True)

    @property
    def add(self):
        self.quantity = self.quantity + 1
        self.save()

    @property
    def sub(self):
        self.quantity = self.quantity - 1
        self.save()


    def __str__(self):
        return self.id
