from django.db import models
from django.db.models.fields import CharField, TimeField

    
class Salon(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    number=models.IntegerField()
    rating=models.DecimalField(max_digits=10,decimal_places=1)

    def __str__(self):
       return f"{self.name}{self.address}"

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'

    


class SalonServices(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    duration=models.IntegerField()
    salon=models.ForeignKey(Salon,on_delete=models.CASCADE)


    def __str__(self):
       return f"{self.name}{self.price}"

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'




class Employee(models.Model):
    name=models.CharField(max_length=200)
    service=models.ManyToManyField(SalonServices)

    def __str__(self):
       return f"{self.name}{self.service}"

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class EmployeeSchedule(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    date=models.DateField()
    start_hour=models.TimeField()
    end_hour=models.TimeField()

    def __str__(self):
       return f"{self.employee}{self.date}{self.start_hour},{self.end_hour}"

    class Meta:
        verbose_name = 'График работы'
        
