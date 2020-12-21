from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),  #localhost/users/
    path("home/",views.home),  #localhost/users/home
    path("login/",views.login),  #localhost/users/login --> /users/signin
    path("signup/",views.signup),
    path("aftersignup/",views.aftersignup),
    path("afterlogin/",views.afterlogin.as_view()),
    path("logout/",views.logout),
    path("forgot/",views.forgot),
   
    
    
    
]