from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.handellogin , name='login'),
    path('singin/', views.singin, name ='singin'),
    path('logout/',views.handellogout,name='logout'),
    
]
