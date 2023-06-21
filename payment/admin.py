from django.contrib import admin
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("name","price","total","image")
admin.site.register(Payment,PaymentAdmin)

