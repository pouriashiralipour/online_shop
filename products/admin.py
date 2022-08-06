from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status', 'active', ]

    def __str__(self):
        return f'{self.title}'

