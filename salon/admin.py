from django.contrib import admin
from .models import EmployeeSchedule, Salon, SalonServices,Employee,EmployeeSchedule

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','number','rating']
    list_filter = ('name','address', 'rating')

@admin.register(SalonServices)
class SalonServicesAdmin(admin.ModelAdmin):
    list_display = ['salon','name','price','duration']
    list_filter = ('salon', 'name','price','duration')
    

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ('name', 'service')

@admin.register(EmployeeSchedule)
class EmployeeScheduleAdmin(admin.ModelAdmin):
    list_display = ['employee','date','start_hour','end_hour']
    list_filter = ('employee','date','start_hour','end_hour')
