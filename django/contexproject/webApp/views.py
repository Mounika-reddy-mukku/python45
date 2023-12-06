from django.shortcuts import render
import datetime
# Create your views here.

def indexpage(req):
    eid=101
    ename="Mounika"
    esal=55000
    return render(req,'index.html',context={'eid':eid,'ename':ename,'esal':esal})

def contactpage(req):
    CT=datetime.datetime.now()
    return render(req,'contact.html', context={'ct':CT})

