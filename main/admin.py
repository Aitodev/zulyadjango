from django.contrib import admin
from .models import Product, Categories, Materials, Colors, Sizes


class CategoriesConfig(admin.ModelAdmin):
    fields = ('name', 'slug_category')
    prepopulated_fields = {'slug_category': ('name',)}
    list_display = fields


admin.site.register(Categories, CategoriesConfig)


class SizesConfig(admin.ModelAdmin):
    fields = ('name',)
    list_display = fields


admin.site.register(Sizes, SizesConfig)


class MaterialsConfig(admin.ModelAdmin):
    fields = ('name',)
    list_display = fields


admin.site.register(Materials, MaterialsConfig)


class ColorsConfig(admin.ModelAdmin):
    fields = ('name', 'color')
    list_display = fields


admin.site.register(Colors, ColorsConfig)


class ProductConfig(admin.ModelAdmin):
    fields = ('name',
              'category',
              'img',
              'price',
              'materials',
              'colors',
              'sizes',
              )
    list_display = ('name', 'category', 'price')


admin.site.register(Product, ProductConfig)
