from django.db import models
from coupon_app.models import Coupon

class Customer(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name="First Name",
        help_text="Enter the first name of the customer."
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Last Name",
        help_text="Enter the last name of the customer."
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Phone Number",
        help_text="Enter the phone number of the customer."
    )
    source_x = models.FloatField(
        verbose_name="Source X Coordinate",
        help_text="Enter the X coordinate of the customer's source location."
    )
    source_y = models.FloatField(
        verbose_name="Source Y Coordinate",
        help_text="Enter the Y coordinate of the customer's source location."
    )
    destination_x = models.FloatField(
        verbose_name="Destination X Coordinate",
        help_text="Enter the X coordinate of the customer's destination."
    )
    destination_y = models.FloatField(
        verbose_name="Destination Y Coordinate",
        help_text="Enter the Y coordinate of the customer's destination."
    )
    trip_type = models.CharField(
        max_length=20,
        verbose_name="Trip Type",
        help_text="Enter the type of the trip (e.g., standard, premium)."
    )
    coupons = models.ForeignKey(
        Coupon,
        on_delete=models.PROTECT,
        verbose_name="Coupon",
        help_text="Select the coupon associated with the customer."
    )
    availability = models.BooleanField(
        verbose_name="Availability",
        help_text="Indicate if the customer is available for trips."
    )

    wallet = models.FloatField(verbose_name="Wallet",default=0)
    def __str__(self) -> str:
        return self.first_name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
