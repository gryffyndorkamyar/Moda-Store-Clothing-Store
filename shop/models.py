from django.db import models
#from rest_framework.authtoken.admin import User
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from Tools.demo.mcast import sender
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    pprice = models.CharField(max_length=100, null=True)
    osale = models.BooleanField(default=False)
    sale_price = models.CharField(default=False, max_length=100, null=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    shopimage = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    productname = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    shop = models.ManyToManyField(Shop)
    price = models.PositiveBigIntegerField(null=True , blank=True)
    productimage = models.ImageField(upload_to='images/', null=True)
    description = models.CharField(max_length=300 , null=True , blank=True)

    Size_Ha = (
        ('s',30)
        ,('m',32)
        ,('l',34)
        ,('xl',36)
    )
    size_Ha = models.CharField(max_length=100,choices=Size_Ha , null=True)
    is_sale_forthisproduct = models.BooleanField(default=False)
    sale_price_forthisproduct = models.PositiveBigIntegerField( null=True, blank=True)

    def __str__(self):
        return self.productname


class Order(models.Model):
    colour = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ManyToManyField(Shop)
    numerquant = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.colour


class Costumer(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    Costumerimage = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User , auto_now=True)
    phone = models.CharField(max_length=25 , blank=True)
    address = models.CharField(max_length=250 , blank=True)
    address1 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=25 , blank=True)
    state = models.CharField(max_length=25 , blank=True)
    country = models.CharField(max_length=25 , default='IRAN')
    zip = models.CharField(max_length=25 , blank=True)

    def __str__(self):
        return self.user.username

def created_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(created_profile, sender=User)


class Comment(models.Model):
     mahsool = models.CharField(max_length=100)
     person = models.CharField(max_length=100)
     product = models.ManyToManyField(Product)
     text = models.CharField(max_length=100)
     gif = models.ImageField(upload_to='images/', null=True)

     def __str__(self):
         return self.mahsool




