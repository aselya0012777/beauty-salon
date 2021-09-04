from django.db import models
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save

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
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=11)
    service = models.ForeignKey(SalonServices,on_delete=CASCADE)
    note = models.TextField()
    appoinmentDate = models.DateField()
    appoinmentTime = models.TimeField()  
    applyDate = models.DateTimeField(auto_now_add=True)
    remarkDate = models.DateTimeField(auto_now=True)
    appointmentNumber = models.IntegerField(null=True, blank=True)
    REMARK_CHOICES = (
        ('1', 'Accepted'),
        ('0', 'Rejected'),
    )
    remark = models.CharField(max_length=1, choices=REMARK_CHOICES)
    def __str__(self):
        return self.Name

@receiver(post_save, sender=Appointment)
def appointment_listing_update(sender, instance, created, **kwargs):
    appointmentnumber = 6000
    if created:
        instance.AppointmentNumber = appointmentnumber + instance.id
        instance.save()


    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    


