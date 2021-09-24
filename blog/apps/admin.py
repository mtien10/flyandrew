from django.contrib import admin
from blog.apps.models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")


# admin.site.register(Category)


admin.site.register(Product)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customerAddress", "orderDate", "product")


# admin.site.register(Order)
