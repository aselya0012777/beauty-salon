from django.db import models
from salon.models import Salon, SalonServices, Employee

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 200)
    phone_number = models.IntegerField()

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Appointment(models.Model):
    date=models.DateField()
    time= models.TimeField()
    salon=models.ForeignKey(Salon, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    service=models.ForeignKey(SalonServices,on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    duration=models.TimeField()

    def __str__(self):
        return f"{self.salon}{self.service}{self.date}{self.time}"

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    


