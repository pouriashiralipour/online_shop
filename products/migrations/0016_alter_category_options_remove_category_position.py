# Generated by Django 4.0.2 on 2022-08-20 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_comments_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['parent__id'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='position',
        ),
    ]
