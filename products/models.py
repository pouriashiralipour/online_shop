from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    STATUS_CHOICES = (
        ('ava', 'available'),
        ('nav', 'not_available'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default='ava')
    cover = models.ImageField(upload_to='covers/', blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_details_view', args=[self.id])


class Comments(models.Model):
    PRODUCT_STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('product_details_view', args=[self.product.id])
