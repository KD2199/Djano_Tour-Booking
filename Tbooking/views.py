from django.shortcuts import render,redirect
from Tbooking.models import Messages,City,Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User,auth
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


@login_required
def contact(request):
   
   if request.method =='POST':

        username=request.POST['uname']
        subject=request.POST['sub']
        message=request.POST['msg']
        email=request.POST['email']
        obj=Messages.objects.get_or_create(UserName=username,Subject=subject,Message=message,Email=email)
        messages.success(request,"WE Will Contact YOU Soon!")
    

   return render(request, 'index.html')

@login_required
def msg(request):

    obj = Messages.objects.all()

    return render(request, 'amsg.html', {'obj': obj})

@login_required
def offer(request):

    obj = City.objects.all()

    return render(request, 'offer.html', {'obj': obj})


@login_required
def book(request,places_pk):

    uname = request.user
    print(uname)
    obj = City.objects.filter(pk=places_pk)
    udata = User.objects.filter(username=uname)
    for nm in udata:
        email=nm.email
        for i in obj:
            data=Order.objects.get_or_create(UserName=uname,Email=email,CityName=i.CityName,Total=i.Price,Booking_date=datetime.now(),Depart_date=i.Depart_date)
    messages.success(request,"Booking Successfully!!")
    return redirect("/")


@login_required
def booking_list(request):
    
    obj = Order.objects.all()
    return render(request, 'booking_list.html', {'obj': obj})