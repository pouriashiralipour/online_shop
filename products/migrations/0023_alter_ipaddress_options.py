# Generated by Django 4.0.2 on 2022-08-23 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_ipaddress_alter_category_options_product_hits'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipaddress',
            options={'verbose_name': 'IP address', 'verbose_name_plural': 'IP addresses'},
        ),
    ]
