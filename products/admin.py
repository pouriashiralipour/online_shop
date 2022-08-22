from django.contrib import admin
from django.contrib import messages
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ngettext

from .models import Product, Comments, Category, IPAddress


@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ['ip_address']


class CommentInline(admin.StackedInline):
    model = Comments
    fields = ['author', 'text', 'stars', 'is_active', 'recommend']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover_img', 'slug', 'category_display', 'price', 'status', 'active', ]
    ordering = ('datetime_created',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_not_available', 'make_available', 'make_active', 'make_de_active']
    list_per_page = 25
    inlines = [
        CommentInline,
    ]

    @admin.action(description=_('Selected products are not available'))
    def make_not_available(self, request, queryset):
        updated = queryset.update(status='nav')
        self.message_user(request, ngettext(
            _('%d story was successfully marked as not available.'),
            _('%d stories were successfully marked as not available.'),
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description=_('Selected products are active'))
    def make_active(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as activated.'),
            _('%d stories were successfully marked as activated.'),
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description=_('Selected products are de_active'))
    def make_de_active(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as deactivated.'),
            _('%d stories were successfully marked as deactivated.'),
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description=_('Selected products are available'))
    def make_available(self, request, queryset):
        updated = queryset.update(status='ava')
        self.message_user(request, ngettext(
            _('%d story was successfully marked as available.'),
            _('%d stories were successfully marked as available.'),
            updated,
        ) % updated, messages.SUCCESS)

    def category_display(self, obj):
        return " ، ".join([category.title for category in obj.category.all()])

    category_display.short_description = _("categories")


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'text', 'stars', 'is_active', 'recommend']
    ordering = ('datetime_created',)
    list_per_page = 25
    search_fields = ('author',)
    actions = ['make_active', 'make_de_active']

    @admin.action(description=_('Selected products are active'))
    def make_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as activated.'),
            _('%d stories were successfully marked as activated.'),
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description=_('Selected products are de_active'))
    def make_de_active(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as deactivated.'),
            _('%d stories were successfully marked as deactivated.'),
            updated,
        ) % updated, messages.SUCCESS)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'parent', 'datetime_created']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_de_active', 'make_active']
    ordering = ['datetime_created']

    @admin.action(description=_('Selected categories are de_active'))
    def make_de_active(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as deactivated.'),
            _('%d stories were successfully marked as deactivated.'),
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description=_('Selected categories are active'))
    def make_active(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            _('%d story was successfully marked as deactivated.'),
            _('%d stories were successfully marked as deactivated.'),
            updated,
        ) % updated, messages.SUCCESS)
