from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('product_details_view', args=[self.id])
