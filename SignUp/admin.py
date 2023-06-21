from django.contrib import admin

from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ("name","email_address","username","password","passsword_confirmation")
admin.site.register(SignUp,SignUpAdmin)

