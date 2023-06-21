from django.db import models


class Cart(models.Model):
    name = models.CharField(max_length = 32)
    quantity = models.PositiveIntegerField()
    total =  models.PositiveIntegerField()
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    