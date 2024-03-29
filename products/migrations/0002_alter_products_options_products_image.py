# Generated by Django 4.0.2 on 2023-08-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-datetime_created'], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='covers/', verbose_name='image'),
        ),
    ]
