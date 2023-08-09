from django.db import models
from django.conf import settings
from django.utils.translation import gettext, gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))
    is_paid = models.BooleanField(default=False, verbose_name=_('is_paid'))

    first_name = models.CharField(max_length=100, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last_name'))
    phone_number = models.CharField(max_length=15, verbose_name=_('phone_number'))
    address = models.CharField(max_length=700, verbose_name=_('address'))

    order_note = models.TextField(verbose_name=_('order_note'), blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    def __str__(self):
        return f'Order {self.id}'

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        ordering = ['-datetime_created']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('order'))
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE, related_name='order_items', verbose_name=_('product'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('quantity'))
    price = models.PositiveIntegerField(verbose_name=_('price'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} x {self.quantity} (price:{self.price})'

    class Meta:
        verbose_name = _('order_item')
        verbose_name_plural = _('order_items')
        ordering = ['-datetime_created']


