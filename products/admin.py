from django.contrib import admin

from .models import Product, Comments


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status', 'active', ]


@admin.register(Comments)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'text', 'stars', 'is_active', 'recommend']

