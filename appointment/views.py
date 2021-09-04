from salon.models import Salon, SalonServices
from django.shortcuts import redirect, render
from django.urls import reverse

def make_appointment(request):
    if request.method =="POST":
        your_name=request.POST['your-name']
        your_phone=request.POST['your-phone']
        your_email=request.POST['your-email']
        
        # your_employee=request.POST.get('employee',False)
        # appointment_date=request.POST.get('service',False)
     

        return render(request, 'book.html',{
            'your_name':your_name,
            'your_phone':your_phone,
            'your_email':your_email,
            
            # 'employee': employee,
            # 'date':date,
          
            # 
            })

def home(request):

    """
        Provides the ability to make an appoinment via user
    """
    services = SalonServices.objects.all()
    form     = AppoinmentForm(request.POST or None)
      
    if request.method=='POST':
       
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            form.save_m2m()
         
            return redirect(reverse("thankyou", kwargs={
                'id': form.instance.id
            }))

    context={
 
            'form':form,
            'services':services,
            }
    return render(request,'salon/index.html',context)

