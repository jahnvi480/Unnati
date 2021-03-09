from django.contrib import admin

# Register your models here.
from .models import Product ,Cart , CartQty ,Address

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartQty)
admin.site.register(Address)