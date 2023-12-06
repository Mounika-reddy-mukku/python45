
from django.urls import path
from firstApp import views

urlpatterns=[
    path('home1/',views.firstfunct),
    path('home/',views.getFirstpage)
]