from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Login,Signup,Forgot,Getotp #import Login class from forms file in pwd 
from django.views import View
from users.models import Adduser
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
            return render(request,"blogpg.html")
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
                    return render(request,"blogpg.html")
                    #return HttpResponse("welcome")
                else:
                    error = "Incorrect Password....."
                    form = Login()
                    return render(request,"login.html",{'form':form,'error':error})

def logout(request):
    del request.session['email']
    del request.session['islogin']
    form = Login()
    return render(request,"login.html",{'form':form})

def forgot(request):
    form = Forgot()
    return render(request,"forgot.html",{'form':form})

def getotp(request):
    form = Forgot(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        try:
            obj = Adduser.objects.get(email=email)
        except:
            error = "Enter the valid email"
            form = Forgot()
            return render(request,"forgot.html",{'form':form,'error':error})
        else:
            subject = "One time OTP password"
            otp = randint(1000,9999)
            message = f"Your OTP for password change is : {otp}"
            from_email = "daminipal1234@gmail.com"
            to_email = email 
            password = "daminimonu"
            try:
                send_mail(subject,message,from_email,[to_email],fail_silently=False)
                #send_mail(subject,message,from_email,[to_email],auth_password=settings.EMAIL_HOST_PASSWORD)
            except Exception as e:
                return HttpResponse(e)
            else:
                request.session['otp'] = otp
                form = Getotp()
                return render(request,"afterotp.html",{'form':form})

                #return HttpResponse(f"Success ... otp is : {otp}")
    else:
        error = "Invalid form"
        form = Getotp()
        return HttpResponse("Invalid form")


def checkotp(request):
    form = Getotp(request.POST)
    if form.is_valid():
        otp = form.cleaned_data['otp']
        #print(request.session.get("otp"))
        if otp == str(request.session.get("otp")):
            del request.session['otp']
            return HttpResponse("Otp is matched")
        else:
            del request.session["otp"]
            return HttpResponse("OTP does not matched")
    else:
        error = "Invalid form"
        del request.session["otp"]
        form = Getotp()
        return render(request,"afterotp.html",{'form':form,'error':error})

def profile(request):
    displayuser = Adduser.objects.all()
    return render(request,"profile.html",{"Adduser":displayuser})

def delete(request, id):
    displayuser = Adduser.objects.get(id=id)
    displayuser.delete() # change here
    return redirect("/profile")






  




  



#myproject
#manage.py
#blog
#users --> templates
#templates (html pages)
#static (css,images)


