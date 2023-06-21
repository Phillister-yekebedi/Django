from django.contrib import admin

from .models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ("name","quantity","total","price")
admin.site.register(Cart,CartAdmin)

