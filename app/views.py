from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.http import JsonResponse
from django.db.models import Q
from .models import *


def home(request):
    context={}
    p=Product.objects.all()

    context.update({"pro":p})



    return render(request, 'app/home.html',context)

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username').strip().lower()
        
        password =request.POST.get('password').strip()

    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            # print("login successfully")

            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("something went grong")
            messages.info(request, 'Username OR password is incorrect')
            return redirect('/login')
        


    return render(request, 'app/login.html')

def customerregistration(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip().lower() 
        password =request.POST.get('password').strip()
        repassword =request.POST.get('repassword').strip()

        print(email)


    return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')



def logoutUser(request):
    logout(request)
    return redirect('/')