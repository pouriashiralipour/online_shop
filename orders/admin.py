from django.contrib import admin, messages
from django.utils.translation import gettext, gettext_lazy as _, ngettext
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


class OrderInlines(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'quantity', 'price']
    extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'is_paid', 'datetime_created']
    search_field = ('user', 'first_name', )
    inlines = [
        OrderInlines,
    ]


@admin.register(OrderItem)
class CommentsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'datetime_created']
    search_field = ('order', )
