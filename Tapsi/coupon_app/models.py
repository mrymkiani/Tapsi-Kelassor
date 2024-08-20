from django.db import models

class Coupon(models.Model):
    title = models.CharField(max_length=50)
    expire_date = models.DateField()
    percent = models.FloatField()
    coupon_availability = models.BooleanField()

    def __str__(self) -> str:
        return self.title