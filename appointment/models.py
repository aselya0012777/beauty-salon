from django.db import models
from salon.models import Salon

class Appointment(models.Model):
    appointment_id= models.IntegerField()
    appointment_date=models.DateField()
    appointment_time= models.TimeField()
    salon=models.ForeignKey(Salon, on_delete=models.CASCADE)
    customer=models.CharField(max_length=200)
    service=models.CharField(max_length=200)
    employee=models.CharField(max_length=200)
    duration=models.TimeField()
    price=models.IntegerField()


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 200)
    phone_number = models.IntegerField()
    
