from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'salon'
urlpatterns = [
    path('',views.salons_list, name= "salons_list"),
    path('salon_detail/<int:id>/',views.salon_detail, name= "salon_detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
