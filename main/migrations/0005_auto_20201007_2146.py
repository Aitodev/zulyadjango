# Generated by Django 3.0 on 2020-10-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201007_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug_product',
            field=models.SlugField(verbose_name='URL'),
        ),
    ]
