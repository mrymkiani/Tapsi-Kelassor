from django.db import models
from coupon_app.models import Coupon


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    source_x = models.FloatField()
    source_y = models.FloatField()
    destination_x = models.FloatField()
    destination_y = models.FloatField()
    trip_type = models.CharField(max_length=20)
    coupons = models.ForeignKey(Coupon, on_delete=models.PROTECT)
    availability = models.BooleanField()

    def __str__(self) -> str:
        return self.first_name
