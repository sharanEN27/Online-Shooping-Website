# Generated by Django 4.0.2 on 2022-02-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop', '0005_alter_product_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Ratings',
            field=models.TextField(max_length=100, verbose_name='0/5'),
        ),
    ]
