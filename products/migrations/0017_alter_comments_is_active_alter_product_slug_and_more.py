# Generated by Django 4.0.2 on 2022-08-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_category_options_remove_category_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=500, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=500, verbose_name='title'),
        ),
    ]
