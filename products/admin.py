from django.contrib import admin
from django.contrib import admin, messages
from django.utils.translation import gettext, gettext_lazy as _, ngettext
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Products, Comments


class CommentsInline(admin.TabularInline):
    model = Comments
    fields = ['user', 'text', 'stars', 'is_active', 'recommend']
    extra = 1


@admin.register(Products)
class ProductsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'cover_img', 'slug', 'price', 'status', 'active', 'datetime_created']
    search_field = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_not_available', 'make_available', 'make_active', 'make_de_active']
    inlines = [
        CommentsInline,
    ]

    @admin.action(description=_('Selected products are not available'))
    def make_not_available(self, request, queryset):
        updated = queryset.update(status='not')
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


@admin.register(Comments)
class CommentsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'product', 'is_active', 'recommend', 'stars', 'datetime_created']
    search_field = ('product',)
