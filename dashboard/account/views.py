from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from . models import *
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
# Create your views here.


def handellogin(request):
    
    if request.method=='POST':
        logusername = request.POST.get('username')
        logpassword = request.POST.get('password')

        user = authenticate(username = logusername,password = logpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Login")
            return redirect("/")  
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect("/")

    return render(request,'login.html')


def handellogout(request):
    logout(request)
    messages.success(request,"Sucessfully Logout")
    return redirect("/")



def singin(request):
    if request.method=="POST":
        type = request.POST.get('type')
        fname =request.POST.get('fname')
        lname =request.POST.get('lname')
        email =request.POST.get('email')
        profile_pic = request.POST.get('fileupload')
        password =request.POST.get('password')
        password2 =request.POST.get('password2')
        address =request.POST.get('address')
        city =request.POST.get('city')
        state =request.POST.get('state')
        pincode =request.POST.get('pincode')
        username =request.POST.get('username')
        if password != password2:
            messages.warning(request,"Password dont match")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        obj = detail( type = type, fname = fname , lname = lname , email = email , profile_pic = profile_pic , password = password , address = address , city = city , state = state ,pincode = pincode , username = username)
        
       
        
        obj.save()
        return redirect('/')
   
 
    return render(request,'singin.html')