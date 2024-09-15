from django.db import models
from customer_app.models import Customer
from coupon_app.models import Coupon
from django.contrib.auth.models import User

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey('driver_app.Driver', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    payment_status = models.BooleanField()
    trip_cost = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.trip_id)


class Message(models.Model):
    sender = models.ForeignKey(User , related_name='sent_massege', on_delete=models.CASCADE)
    reciver = models.ForeignKey(User , related_name= 'recived_massage', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    
    