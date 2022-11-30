from itertools import product
from unicodedata import category
from django.contrib import admin
from ecommerce.inventory import models

admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Media)
admin.site.register(models.ProductInventory)
admin.site.register(models.Collection)