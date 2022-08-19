from django.contrib import admin

from .models import Product, Comments


class CommentInline(admin.StackedInline):
    model = Comments
    fields = ['author', 'text', 'stars', 'is_active', 'recommend']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'status', 'active', ]
    ordering = ('datetime_created', )
    search_fields = ('title',)
    list_per_page = 25
    inlines = [
        CommentInline,
    ]


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'text', 'stars', 'is_active', 'recommend']
    ordering = ('datetime_created', )
    list_per_page = 25
    search_fields = ('author', )

