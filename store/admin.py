from django.contrib import admin

from store import models


@admin.register(models.Product)
class ProductModel(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10


@admin.register(models.Customer)
class CustomerModel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']


admin.site.register(models.Collection)
