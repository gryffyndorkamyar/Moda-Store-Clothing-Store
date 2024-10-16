from django.contrib import admin
from django.contrib.auth.models import User

from shop.models import Category
from shop.models import Costumer
from shop.models import Order
from shop.models import Comment
from shop.models import Shop
from shop.models import Product
from shop.models import Profile
from . import models


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'city']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'productname', 'price']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'numerquant', 'colour']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'person']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Costumer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(models.Profile)


class ProfileinLine(admin.StackedInline):
    model = models.Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'firstname', 'lastname', 'email']
    inLines = [ProfileinLine]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
