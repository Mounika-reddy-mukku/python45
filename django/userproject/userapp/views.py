from django.shortcuts import render
from userapp.models import user
# Create your views here.

def getuserdetails(request):
    user_list=user.objects.all()
    return render(request,'user.html' ,context={'users':user_list})
