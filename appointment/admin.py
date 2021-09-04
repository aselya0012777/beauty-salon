from appointment.models import Appointment
from django.contrib import admin
from .models import Customer, Appointment

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone_number','email']
    list_filter = ('first_name','last_name','phone_number','email')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name','email','phoneNumber','service','note','appoinmentDate','appoinmentTime','applyDate','remarkDate','appointmentNumber','remark']
    list_filter = ('name','email','phoneNumber','service','note','appoinmentDate','appoinmentTime','applyDate','remarkDate','appointmentNumber','remark')

