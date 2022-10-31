from . models import *
from account.models import *
from django.shortcuts import render

# Create your views here.

def home(request):

    obj = detail.objects.all()
    data = {
        'obj':obj
    }
    return render(request,'home.html',data)


def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mess = request.POST.get('message')

        obj = Contact_us( name = name , email = email, phone = phone, mess = mess)
        obj.save()

    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

def slug(request,uid):

    obj = detail.objects.filter(uid = uid)
    print(obj)

    data = {
        'obj':obj
    }
    return render(request,'slug.html',data)

