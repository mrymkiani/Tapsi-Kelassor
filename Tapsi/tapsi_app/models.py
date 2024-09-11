from django.db import models
from driver_app.models import Driver
from customer_app.models import Customer
from coupon_app.models import Coupon

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    payment_status = models.BooleanField()
    trip_cost = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.trip_id)
