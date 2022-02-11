from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.views.generic.list import ListView
# from hitcount.views import HitCountDetailView
from django.db.models.expressions import F
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, View


# from ssf.models import BlogPost, VideoUpload, project_image
# from ssf.models import *
# from paypal_payment.models import *
from common.models import *

# Create your views here.



import datetime


class MainSitemap(TemplateView):
    template_name = 'sitemap/sitemap.xml'
    content_type = 'text/xml'

    def get(self, request):
        context = self.get_context_data()

        urlmap = Sitemap.objects.all()
        context['urlmap'] = urlmap

        return self.render_to_response(context)




def show_ads(request,id):

    now = datetime.datetime.now() 
    data=SponsorAd.objects.filter(pk=id).last().body

    msg = f'Today is {now}'

    return HttpResponse(data)

# def home(request): 
#     context={}
#     return render(request,'login/login.html' , context)


def login_user(request): 
    # dd=project_image.objects.values("image","slug")
    urll=request.build_absolute_uri()
    pth=urll.split("login_user/?next=")
    url=pth[-1]
    print(urll,urll,urll,urll,type(urll))
    context={}
    # context.update(base_data())
    print("******************************",request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        
        password =request.POST.get('password')

        if username is not None and password is not None:
            print(username,password ,"**************************************")
            user = authenticate(request, username=username.lower().strip(), password=password.strip())
            if user is not None:
                login(request, user)
                print("logedin successfully")
                return redirect('/')            #home dashboard have to create function url page for dashboard
            else:
                usr=User.objects.filter(username=username)
                if usr.exists():
                    messages.info(request,"Password incurrect forgot password to recover your account")
                    print("Password incurrect forgot password to recover your account")
                    return redirect(url)
                else:
                    print("seems does not signup yet")
                    messages.info(request, 'Username OR password is incorrect')
                    return redirect('/login_user')
        else:
            email = request.POST.get('email')
            password1 =request.POST.get('password1')
            print(email,password1,"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            usr,created=User.objects.get_or_create(username=email,email=email, is_staff=True) 
            if created:
                # pswd=RecoverPass(user=usr,password=password1)
                # pswd.save()
                usr.set_password(password1)  
                usr.save()
                # usr.groups.add(4)  # adding group= "studnt" id of group is 4
                # user_id = usr.pk
                messages.success(request,"User created successfully")
                print("User created successfully")
                return redirect(url)                
            else:
                messages.info(request,"Already This account forgot password to recover your account")
                print("forgot password to recover your account")
                return redirect(url)

            print(usr)
            #u = User.objects.get(username=new_user_name)
            # u.set_password('temporary')


       

        
           
    
    return render(request,'login/login.html' , context)


@login_required(login_url='login_user')
def home(request): 
    username = request.user.username
    context={"user":username}

    return render(request,'dashboard.html' , context)


def home2(request): 
    username = request.user.username
    context={"user":username}

    return render(request,'AdminLite1/index.html' , context)



def logoutUser(request):
    logout(request)
    return redirect('home')

def signup(request): 
    # dd=project_image.objects.values("image","slug")
    urll=request.build_absolute_uri()
    pth=urll.split("login_user/?next=")
    url=pth[-1]
    print(urll,urll,urll,urll,type(urll))
    context={}
    # context.update(base_data())
    if request.method == 'POST':
        username = request.POST.get('username').strip().lower()
        
        password =request.POST.get('password').strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(url)
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('/signup')
           
    
    return render(request,'login/register.html' , context)




def forgot_password(request): 
    # dd=project_image.objects.values("image","slug")
    urll=request.build_absolute_uri()
    pth=urll.split("login_user/?next=")
    url=pth[-1]
    print(urll,urll,urll,urll,type(urll))
    context={}
    # context.update(base_data())
    if request.method == 'POST':
        username = request.POST.get('username').strip().lower()
        
        password =request.POST.get('password').strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(url)
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('/forgot_password')
           
    
    return render(request,'login/forgot_password.html' , context)