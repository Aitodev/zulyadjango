# Generated by Django 3.0 on 2020-10-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201006_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug_product',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
    ]