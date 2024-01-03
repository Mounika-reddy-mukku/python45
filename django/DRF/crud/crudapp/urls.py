from django.contrib import admin
from django.urls import path
from crudapp import views
urlpatterns=[ 
    path('add/',views.createemp),
    path('update/<int:id>',views.updateemp),
    path('',views.reademp),
    path('delete/<int:id>',views.deleteemp)
]