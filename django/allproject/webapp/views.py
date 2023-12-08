from django.shortcuts import render
from webapp.forms import Form1
# Create your views here.
def gethomepage(request):
    return render(request,'home.html')

def getaboutpage(request):
    return render(request,'about.html')

def getregisterpage(request):
    form=Form1()
    

    return render(request,'register.html',{'form':form})

def getloginpage(request):
    return render(request,'login.html')

def savepage(request):
    return render(request,'save.html')