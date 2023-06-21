from django.contrib import admin

from .models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("name","payments","items","email_adress","pick_up_point")
admin.site.register(Delivery,DeliveryAdmin)
