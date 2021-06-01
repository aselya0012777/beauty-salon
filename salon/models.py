from django.db import models
from django.db.models.fields import CharField

class Salon(models.Model):
    salon_name=models.CharField(max_length=200)
    salon_address=models.CharField(max_length=300)
    salon_services=models.CharField(max_length=250)
    salon_number=models.IntegerField
    salon_rating=models.IntegerField(max_digit=10)


class SalonServices(models.Model):
    service_id=models.IntegerField()
    service_name=models.CharField(200)
    service_price=models.IntegerField()
    service_duration=models.TimeField()
    

class Employee(models.Model):
    employee_id=models.IntegerField()
    name=models.CharField(max_length=200)
    service=models.CharField(200)