from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'appointment'
urlpatterns = [
   path('make-appointment/', views.make_appointment, name= "book")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
