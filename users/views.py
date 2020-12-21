from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup,Forgot,Getotp #import Login class from forms file in pwd 
from django.views import View
from .models import Adduser
from random import randint
from django.core.mail import send_mail
from django.conf import settings


  # Create your views here.

def index(request):
    #return HttpResponse("Welcome to my users app")
    return render(request,"index.html")

def home(request):
    return HttpResponse("THIS IS MY HOME OF DJANGO")

def login(request):
    form = Login()
    return render(request,"login.html",{'form':form})

def signup(request):
    form = Signup()
    return render(request,"signup.html",{'form':form})

def aftersignup(request):
    form = Signup(request.POST)
    if form.is_valid(): 
        name = form.cleaned_data['fullname']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        Adduser.objects.create(fullname=name,email=email,password=password)
        form = Login()
        return render(request,"login.html",{'form':form})
    else:
        error = "invalid form"
        form = Signup()
        return render(request,"signup.html",{'form':form})
    return render()

class afterlogin(View):
    def get(self,request):
        if request.session.get("email"):
            return render(request,"addblog.html")
        else:
            error = "No such method allowed"
            form = Login()
            return render(request,"login.html",{'form':form,'error':error})

    def post(self,request):
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                obj = Adduser.objects.get(email=email)
            except:
                error = "No such user"
                form = Signup()
                return render(request,"signup.html",{'form':form,'error':error})
            else:
                if obj.password == password:
                    request.session['email'] = email
                    request.session['islogin'] = "true"
                    return render(request,"addblog.html")
                    #return HttpResponse("welcome")
                else:
                    error = "Incorrect Password....."
                    form = Login()
                    return render(request,"signup.html",{'form':form,'error':error})

def logout(request):
    del request.session['email']
    del request.session['islogin']
    form = Login()
    return render(request,"login.html",{'form':form})

def forgot(request):
    form = Forgot()
    return render(request,"forgot.html",{'form':form})



