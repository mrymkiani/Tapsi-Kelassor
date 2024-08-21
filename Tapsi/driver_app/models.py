from django.db import models

class Driver(models.Model):
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
        help_text="Enter the current balance in the driver's wallet."
    )

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
