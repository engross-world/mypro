from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Addblogs
from users.models import Adduser
from .models import Addblog
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("<h1 style='color:red'>Welcome to my blog app</h1>")

def addblog(request):
    form = Addblogs()
    return render(request,"addblog.html",{'form':form})

class addpost(View):
    def post(self,request):
        print("DATA IS POSTING ................")
        form = Addblogs()
        if form.is_valid(): 
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            user = Adduser.objects.get(email="monu@gmail.com")
            Addblog.objects.create(title=title,post=post,user=user)
            form = Addblogs()
            return render(request,"allblog.html",{'form':form})
        else:
            error = "invalid form"
            form = Addblogs()
            return render(request,"addblog.html",{'form':form})




        # form = Addblogs(request.POST)
        # if form.is_valid():
        #     title = form.cleaned_data['title']
        #     post = form.cleaned_data['post']
        #     user = Adduser.objects.get(email=request.session.get("email"))
        #     Addblog.objects.create(title=title,post=post,user=user)
        #     error = "Blog added"
        # return HttpResponse("<h1 style='color:red'>Blog added</h1>")

def myblog(request):
    if request.session.get("email"):
        return HttpResponse("<h1 style='color:red'>GET session email </h1>")
    else:
        return HttpResponse("<h1 style='color:red'>not get </h1>")
    # print("OUTSIDE")
    # if request.method == "GET":
    #     print("INSIDE")
    #     user = Adduser.objects.get(email=request.session.get("email"))
    #     print(user)
    #     blogs = Addblog.objects.filter(user=user.id)
    #     print(blogs)
    #     values = []
    #     for i in blogs:
    #         d = {
    #             "title" : i.title,
    #             "post"  : i.post,
    #             "user"  : i.user.fullname,
    #             "date"  : i.date
    #         }
    #         values.append(d)
    #     print("VLAUES",values)
    #     return render(request,"userblogs.html",{"blogs":values})
    # else:
    #     error = "User post not found"
    #     return render(request,"profile.html",{'error':error})

def allblogs(request):
    # print("OUTSIDE")
    if request.method == "POST":
        # print("INSIDE POST")
        allblog = Addblog.objects.all()[:10]
        values = []
        for i in allblog:
            d = {
                    "title": i.title,
                    "post" : i.post,
                    "user" : i.user.fullname,
                    "date" : i.date
            }
            values.append(d)
        # print("VALUES",values)
        return render(request,"userblogs.html",{'blogs':allblog})
    

def profile(request):
    displayuser = Adduser.objects.all()
    return render(request,"profile.html",{"Adduser":displayuser})

def delete(request, id):
    displayuser = Adduser.objects.get(id=id)
    print(type(displayuser))
    displayuser.delete() # change here
    return redirect("/myblog")
    

    
    








