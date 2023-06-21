from django.db import models

class Delivery(models.Model):
    name = models.CharField(max_length = 32)
    payments = models.DecimalField(max_digits = 9, decimal_places = 2)
    items = models.PositiveIntegerField()
    email_adress = models.CharField(max_length = 32)
    pick_up_point= models.CharField(max_length = 32)
