import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Categories(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    slug_category = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Materials(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Colors(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    color = models.CharField(verbose_name='Код цвета (например #FFFFFF)', max_length=7)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Sizes(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Product(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    slug_product = models.SlugField(verbose_name='URL', unique=True, default=uuid.uuid1)
    category = models.ForeignKey(Categories, verbose_name='Категория', related_name='category',
                                 on_delete=models.PROTECT, blank=True, null=True)
    img = models.ImageField(verbose_name='Изображение 1', upload_to='media/products')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    materials = models.ManyToManyField(Materials, verbose_name='Материалы', related_name='materials')
    colors = models.ManyToManyField(Colors, verbose_name='Цвета', related_name='colors')
    sizes = models.ManyToManyField(Sizes, verbose_name='Размеры', related_name='sizes')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug_product])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

