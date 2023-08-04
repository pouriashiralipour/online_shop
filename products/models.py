import random

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save


class Products(models.Model):
    STATUS_CHOICES = (
        ('ava', _('available')),
        ('not', _('not_available')),
    )
    title = models.CharField(max_length=200, verbose_name=_('title'))
    slug = models.SlugField(max_length=500, unique=True, allow_unicode=True, verbose_name=_('slug'))
    description = models.TextField(verbose_name=_('description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default='ava', verbose_name=_('status'))
    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['-datetime_created']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance


def products_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    # print(sender, instance)
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(products_pre_save, sender=Products)


def products_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    # print(args, kwargs)
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(products_post_save, sender=Products)
