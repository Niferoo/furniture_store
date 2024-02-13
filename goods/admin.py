from django.contrib import admin

from goods.models import Categories
from goods.models import Products


# Register your models here
# admin.site.register(Categories)
#admin.site.register(Products)

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}