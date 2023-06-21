from django.db import models

class SignUp(models.Model):
    name = models.CharField(max_length = 32)
    email_address= models.CharField(max_length = 20)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length= 8)
    passsword_confirmation = models.CharField(max_length = 8)
