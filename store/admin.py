from django.contrib import admin

from store import models


@admin.register(models.Product)
class ProductModel(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        return 'OK'

    def collection_title(self, product):
        return product.collection.title


@admin.register(models.Customer)
class CustomerModel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']


@admin.register(models.Order)
class OrderModel(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']


admin.site.register(models.Collection)
