from django.db import models

class Coupon(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Coupon Title",
        help_text="Enter the title of the coupon."
    )
    expire_date = models.DateField(
        verbose_name="Expiration Date",
        help_text="Enter the expiration date of the coupon."
    )
    percent = models.FloatField(
        verbose_name="Discount Percentage",
        help_text="Enter the discount percentage provided by the coupon."
    )
    percent = models.BooleanField(
        verbose_name="Coupon Availability",
        help_text="Indicate if the coupon is currently available for use."
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"
