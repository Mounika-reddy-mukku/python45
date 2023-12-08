from django.shortcuts import render
from employapp.models import employees
# Create your views here.
def getemploy(req):
    employ=employees.objects.all()
    return render(req,'employ.html', context={'employ':employ})

def gethomepage(req):
    return render(req,'index.html')