from django.db import models
from driver_app.models import Driver
from customer_app.models import Customer


class Trip(models.Model):
    trip_id = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    payment_status = models.BooleanField()
    trip_cost = models.FloatField()
    

    def __str__(self) -> str:
        return self.trip_id
    
