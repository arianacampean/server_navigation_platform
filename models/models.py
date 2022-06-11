from django.db import models

# Create your models here.
class MyUser(models.Model):
    first_name = models.CharField( max_length=150, blank=False)
    last_name = models.CharField( max_length=150, blank=False)
    email = models.EmailField(max_length=150,unique=True,blank=False)
    password = models.CharField(max_length=150,blank=False)

class Journey(models.Model):
    id_user=models.ForeignKey(MyUser, on_delete=models.CASCADE)
    start_date=models.DateTimeField(blank=False)
    end_date=models.DateTimeField(blank=False)


class Trip(models.Model):
    id_journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=40, decimal_places=20)
    longitude = models.DecimalField(max_digits=40, decimal_places=20)
    city = models.CharField(max_length=150, blank=False)
    country = models.CharField(max_length=150, blank=False)
    name = models.CharField(max_length=150, blank=False)
    visited = models.BooleanField(default=False)


