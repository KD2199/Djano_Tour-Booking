
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
import urllib
import json
from django.contrib.auth.decorators import login_required
from Tbooking.models import Messages, Order
from django.core.mail import send_mail


def login(request):

    if request.method == 'POST':

        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if result['success']:
            print("recaptcha validation successfully")
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Successfully!!")
            return redirect('/')

        else:
            messages.success(
                request, "You Have Entered Invalid Username or Password!!")
            return redirect('/')

    return render(request, 'index.html')


def register(request):

    if request.method == 'POST':

        username = request.POST['uname']
        password = request.POST['password']
        password2 = request.POST['pw2']
        email = request.POST['email']

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.success(request, "* username is already registered")

            elif User.objects.filter(email=email).exists():
                messages.success(request, "* Email is already registered")

            else:

                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

                messages.success(request, "Registration Successfully!!")
        
                return redirect('/')
    messages.success(request, "PassWord & Confirm PassWord isn't Same!")
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Successfully!!")
    return redirect('/')


@login_required
def profile(request):
    uname = request.user
    obj = Messages.objects.filter(UserName=uname).count()

    return render(request, 'profile.html', {'obj': obj})


@login_required
def Aprofile(request):
    uname = request.user
    obj1 = User.objects.all().count()-1
    data = Order.objects.all().count()
    return render(request, 'profile.html', {'obj1': obj1, 'data': data})


@login_required
def offer(request):

    return render(request, 'offer.html')


@login_required
def order(request):
    uname = request.user
    obj = Order.objects.filter(UserName=uname).count()
    data = Order.objects.filter(UserName=uname)
    return render(request, 'order.html', {'obj': obj, 'data': data})
