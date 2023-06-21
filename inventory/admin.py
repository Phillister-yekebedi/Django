from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","stock","image","description","date_created","date_updated")
admin.site.register(Product,ProductAdmin)
