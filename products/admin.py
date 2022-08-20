from django.contrib import admin

from .models import Product, Comments, Category


class CommentInline(admin.StackedInline):
    model = Comments
    fields = ['author', 'text', 'stars', 'is_active', 'recommend']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category_display', 'price', 'jalali_published', 'status', 'active', ]
    ordering = ('datetime_created',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 25
    inlines = [
        CommentInline,
    ]

    def category_display(self, obj):
        return " ، ".join([category.title for category in obj.category.all()])


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'text', 'stars', 'is_active', 'recommend']
    ordering = ('datetime_created',)
    list_per_page = 25
    search_fields = ('author',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'position']
    prepopulated_fields = {'slug': ('title',)}
