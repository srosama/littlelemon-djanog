from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

class BookingModel(models.Model):
    name = models.CharField(max_length=255)
    num_of_guests = models.IntegerField( validators=[MaxValueValidator(999999)])
    booking_date = models.DateTimeField(default=timezone.now) 

    def __str__(self) -> str:
        return self.name  

class MenuModel(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return self.title