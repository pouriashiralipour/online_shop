from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


# class Category(models.Model):
#     name = models.CharField(max_length=250, null=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = _('category')
#         verbose_name_plural = _('categories')
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    STATUS_CHOICES = (
        ('ava', 'available'),
        ('nav', 'not_available'),
    )
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'), null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default='ava')
    cover = models.ImageField(upload_to='covers/', blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_details_view', args=[self.id])


class CustomActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(CustomActiveCommentManager, self).get_queryset().filter(is_active=True)


class Comments(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name=_('Comment Text'))
    stars = models.CharField(
        max_length=10,
        choices=PRODUCT_STARS,
        blank=True, null=True,
        verbose_name=_('What is your star?')
    )
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(
        default=True,
        verbose_name=_('I suggest this product')
    )

    # Manager
    objects = models.Manager()
    active_comment_manager = CustomActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_details_view', args=[self.product.id])

