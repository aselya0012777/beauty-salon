from salon.models import Employee, Salon,SalonServices
from django.shortcuts import get_object_or_404, render

def salons_list(request):
    salons = Salon.objects.all()
    services= SalonServices.objects.all()
    return render(request, "index.html", {'salons': salons, 'services': services})


def salon_detail(request,id):
    salon = get_object_or_404(Salon, id=id)
    services=SalonServices.objects.all()
    employees=Employee.objects.all()
    return render(request, 'salon_detail.html', {'salon': salon,'services':services,'employees':employees})

 