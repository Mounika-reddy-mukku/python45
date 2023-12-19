from django.shortcuts import render,redirect
from webapp.forms import Form1,Form2
from webapp.models import registeruser
# Create your views here.
def gethomepage(request):
    return render(request,'home.html')

def getaboutpage(request):
    display=registeruser.objects.all()
    return render(request,'about.html',context={'display_list':display})

def getregisterpage(request):
    if request.method=="POST" :
        regdata=Form1(request.POST)
        if regdata.is_valid():
            regdata.save()
            return redirect('/save')
    else:
        form=Form1()
    return render(request,'register.html',{'form':form})

def updateuser(request,id): 
    userupdate=registeruser.objects.get(id=id)
    if request.method=="POST" :
        regdata=Form1(request.POST)
        if regdata.is_valid():
            regdata.save()
            return redirect('/about')
    return render(request,'update.html',context={'userupdate':userupdate})

def getloginpage(request):
    form=Form2()
    return render(request,'login.html',{'form':form})

def savepage(request):
    return render(request,'save.html')

def deleteuser(request,id):
    user=registeruser.objects.get(id=id)
    user.delete()
    return redirect("/about")