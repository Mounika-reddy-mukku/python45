from django.urls import path
from webapp import views

urlpatterns=[
    path('home/',views.gethomepage),
    path('about/',views.getaboutpage),
    path('register/',views.getregisterpage),
    path('login/',views.getloginpage),
    path('save',views.savepage),
    path('delete/<int:id>',views.deleteuser),
    path('update/<int:id>',views.updateuser)
    
    
]