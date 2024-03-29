# Generated by Django 4.0.2 on 2023-08-05 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_alter_products_options_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('recommend', models.BooleanField(default=True, verbose_name='recommend')),
                ('stars', models.CharField(choices=[('1', 'very Bad'), ('2', 'Bad'), ('3', 'Normal'), ('4', 'Good'), ('5', 'Perfect')], max_length=10)),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='datetime_created')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='datetime_modified')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.products', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ['-datetime_created'],
            },
        ),
    ]
