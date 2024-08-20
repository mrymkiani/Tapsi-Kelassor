from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    car_plate = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    car_model = models.CharField(max_length=50)
    wallet = models.FloatField()


    def __str__(self) -> str:
        return self.first_name