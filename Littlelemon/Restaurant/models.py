from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    Id = models.IntegerField(primary_key=True,validators=[MinValueValidator(1),MaxValueValidator(11)])
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)])
    Booking_date = models.DateTimeField(blank=True)

    

class Menu(models.Model):
    Id = models.AutoField(primary_key=True,validators=[MinValueValidator(1),MaxValueValidator(5)])
    Title = models.CharField(max_length=255)
    Price =models.DecimalField(max_digits=10 , decimal_places=2)
    Inventory = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'


 