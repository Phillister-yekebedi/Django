from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length = 32)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    total = models.DecimalField(max_digits = 6, decimal_places = 3)
    image = models.ImageField()
    
