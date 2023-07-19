from django.db import models
from customer.models import Customer
from Cart.models import Cart
from Delivery.models import Delivery

class Order(models.Model):
    name = models.CharField(max_length = 32)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    total = models.DecimalField(max_digits = 6, decimal_places = 3)
    image = models.ImageField()
    description = models.TextField()

    customer = models.ForeignKey(Customer, null= True, on_delete = models.CASCADE)
    Cart = models.ForeignKey(Cart, null= True, on_delete = models.CASCADE)
    delivery = models.OneToOneField(Delivery, null= True, on_delete=models.CASCADE)








