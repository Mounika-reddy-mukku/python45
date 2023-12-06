from django.urls import path
from staticApp import views

urlpatterns=[
    path('index/',views.indexpage),
    path('about/',views.aboutpage),
    path('contact/',views.contactpage),
    path('service/',views.servicepage)
]