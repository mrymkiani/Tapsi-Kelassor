from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from tapsi_app.models import Trip

class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='drivers')
    first_name = models.CharField(
        max_length=50,
        verbose_name="First Name",
        help_text="Enter the first name of the driver."
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Last Name",
        help_text="Enter the last name of the driver."
    )
    car_color = models.CharField(
        max_length=50,
        verbose_name="Car Color",
        help_text="Enter the color of the driver's car."
    )
    car_plate = models.CharField(
        max_length=50,
        verbose_name="Car Plate Number",
        help_text="Enter the plate number of the driver's car."
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Phone Number",
        help_text="Enter the phone number of the driver."
    )
    car_model = models.CharField(
        max_length=50,
        verbose_name="Car Model",
        help_text="Enter the model of the driver's car."
    )
    wallet = models.FloatField(
        verbose_name="Wallet Balance",
        help_text="Enter the current balance in the driver's wallet.",
        default=0.00
    )
    rating = models.FloatField(verbose_name="Driver Rating", default=0.0) 

    def __str__(self) -> str:
        return self.first_name
    
    def update_rating(self):
        avg_rating = Trip.objects.filter(driver=self, rating__gt=0).aggregate(Avg('rating'))['rating__avg']
        self.rating = avg_rating or 0
        self.save()

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
