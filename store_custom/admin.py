from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from store.admin import ProductModel
from store.models import Product
from tags.models import TaggedItem


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProducttAdmin(ProductModel):
    inlines = [TagInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProducttAdmin)
