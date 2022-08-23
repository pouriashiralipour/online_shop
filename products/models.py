import random
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.html import format_html

from .templatetags import utilis


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name=_('IPAddress'))

    class Meta:
        verbose_name = _('IP address')
        verbose_name_plural = _('IP addresses')


class Category(models.Model):
    parent = models.ForeignKey(
        'self',
        default=None,
        null=True, blank=True,
        verbose_name=_('parent'),
        on_delete=models.SET_NULL,
        related_name='child',
    )
    title = models.CharField(max_length=250, verbose_name=_('title'))
    slug = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True, verbose_name=_('slug'))
    status = models.BooleanField(default=True, verbose_name=_('status'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime_created'), null=True,
                                            editable=True)
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'), null=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS_CHOICES = (
        ('ava', _('available')),
        ('nav', _('not_available')),
    )
    title = models.CharField(max_length=500, verbose_name=_('title'))
    slug = models.SlugField(max_length=500, unique=True, allow_unicode=True, null=True, blank=True,
                            verbose_name=_('slug'))
    category = models.ManyToManyField(Category, verbose_name=_('category'), related_name='products')
    description = models.TextField(verbose_name=_('description'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default='ava', verbose_name=_('status'))
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name=_('cover'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))
    hits = models.ManyToManyField(IPAddress, verbose_name=_('hits'), related_name='hits', blank=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['-datetime_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_details_view', args=[self.slug])

    def category_published(self):
        return self.category.filter(status=True)

    def cover_img(self):
        return format_html("<img width=60 src='{}'>".format(self.cover.url))

    cover_img.short_description = _('image')

    # def jalali_published(self):
    #     return utilis.translate_persian(self.datetime_created)

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


pre_save.connect(products_pre_save, sender=Product)


def products_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    # print(args, kwargs)
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(products_post_save, sender=Product)


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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('product'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', default=1,
                               verbose_name=_('author'))
    text = models.TextField(verbose_name=_('Comment Text'))
    stars = models.CharField(
        max_length=10,
        choices=PRODUCT_STARS,
        blank=True, null=True,
        verbose_name=_('What is your star?')
    )
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))
    is_active = models.BooleanField(default=True, verbose_name=_('active'))
    recommend = models.BooleanField(
        default=True,
        verbose_name=_('I suggest this product')
    )

    # Manager
    objects = models.Manager()
    active_comment_manager = CustomActiveCommentManager()

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['datetime_created']

    def get_absolute_url(self):
        return reverse('product_details_view', args=[self.product.slug])
