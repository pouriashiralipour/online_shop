import random

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from ckeditor.fields import RichTextField


class Products(models.Model):
    STATUS_CHOICES = (
        ('ava', _('available')),
        ('not', _('not_available')),
    )
    title = models.CharField(max_length=200, verbose_name=_('title'))
    slug = models.SlugField(max_length=500, unique=True, allow_unicode=True, verbose_name=_('slug'))
    short_description = RichTextField(verbose_name=_('short_description'), blank=True)
    description = RichTextField(verbose_name=_('description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    image = models.ImageField(upload_to='covers/', verbose_name=_('image'), blank=True)
    active = models.BooleanField(default=True, verbose_name=_('active'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default='ava', verbose_name=_('status'))
    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['-datetime_created']

    def get_absolute_url(self):
        return reverse('products:details_view', args=[self.slug])

    def __str__(self):
        return self.title

    def cover_img(self):
        try:
            return format_html("<img width=60 src='{}'>".format(self.image.url))
        except:
            return ''

    cover_img.short_description = _('image')

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


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(is_active=True)


class Comments(models.Model):
    CHOICES = [
        ('1', _('very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect'))
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',
                             verbose_name=_('user'))
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments', verbose_name=_('product'))
    text = models.TextField(verbose_name=_('text'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))
    recommend = models.BooleanField(default=True, verbose_name=_('recommend'))
    stars = models.CharField(max_length=10, choices=CHOICES, verbose_name=_('star'), null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['-datetime_created']

    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('products:details_view', args=[self.product.slug])

    def __str__(self):
        return f'{self.user}: {self.text}'
