from django.shortcuts import render

# Create your views here.
def indexpage(req):
    return render(req,'index.html')

def aboutpage(req):
    return render(req,'about.html')

def contactpage(req):
    return render(req,'contact.html')

def servicepage(req):
    return render(req,'service.html')


