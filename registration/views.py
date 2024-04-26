from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from registration.models import workers


def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())




def dashboard(request):
    data = workers.objects.all()
    variable={'data':data}
    return render(request, 'dashboard.html', variable)
   # template = loader.get_template('dashboard.html')
    #return HttpResponse(template.render())

@csrf_exempt
def addworker(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['number']
        age = request.POST['age']
        field = request.POST['field']

        mywork={'firstname':firstname, 'lastname':lastname, 'email':email, 'number':phone, 'age':age, 'field':field}
        print(mywork)

        obj2 = workers(first_name=firstname, last_name=lastname, email=email, phone_number=phone, age=age, field=field)
        obj2.save()
#fetchind data from the database
    data=workers.objects.all()
    variable={'data':data}
    return render(request,'dashboard.html',variable)

"""
def editworker(request,id):
   data = workers.objects.get(id=id);
   variable={'data':data}
   return render(request,'update.html',variable)
"""
def updateworker(request, id):
    if request.method == 'POST':
       firstname = request.POST['firstname']
       lastname = request.POST['lastname']
       phonenumber = request.POST['phonenumber']
       age = request.POST['age']
       email = request.POST['email']
       field = request.POST['field']

       editworker = workers.objects.get(id=id)

       #modify the workers details based on the id given
       editworker = workers.objects.get(id=id)
       editworker .first_name =firstname
       editworker.last_name=lastname
       editworker.phone_number=phonenumber
       editworker.email=email
       editworker.age=age
       editworker.field=field
       editworker.save()
    return redirect('/dashboard')

def deleteworker(request, id):
  deleteworker = workers.objects.get(id=id)
  deleteworker.delete()
  return redirect('/dashboard')

def editworker(request, id):
   data = workers.objects.get(id=id);
   variable={'data':data}
   return render(request,'update.html',variable)


# Create your views here.
