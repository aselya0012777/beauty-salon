from django.shortcuts import render

def make_appointment(request):
    if request.method =="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        salon=request.POST.get('salon',False)
        employee=request.POST.get('employee',False)
        date=request.POST.get('service',False)
       

        return render(request, 'book.html',{
            'your_name':name,
            'your_phone':phone,
            'your_email':email,
            'salon':salon,
            'employee': employee,
            'date':date,
          
            })

# def appointment()
