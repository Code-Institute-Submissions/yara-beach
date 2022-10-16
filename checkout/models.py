from django.db import models
from django.contrib.auth.models import User
from datetime import date
import uuid
# Create your models here.

#Contain all orders related to excursions
class ExcursionOrder(models.Model):
    excursion_name = models.CharField(max_length=300, null=False, blank=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, default='')
    order_number = models.CharField(max_length=32, null=False, blank=False, editable=False)
    full_name = models.CharField(max_length=70, null=False, blank=False)
    image = models.URLField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    adult_qty =  models.IntegerField(null=False, blank=False)
    child_qty =  models.IntegerField(null=False, blank=False)
    excursion_date = models.DateField(null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)
    customer_email = models.EmailField(null=True, blank=True)
    cellphone_number = models.CharField(max_length=70, null=True, blank=True)
    place_pickup = models.CharField(max_length=70, null=True, blank=True)


    def _generate_order_number(self):
        """
        Generate a ramdom, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overide the original save method to set the order number
        if it has not been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
