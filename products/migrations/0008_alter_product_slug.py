# Generated by Django 4.0.2 on 2022-08-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_comments_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=500, null=True, unique=True),
        ),
    ]
