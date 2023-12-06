from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstfunct(req):
    return HttpResponse("Hello there!")
 
def getFirstpage(req):
    return render(req,'first.html')