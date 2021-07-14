from django.urls import path
from . import views
urlpatterns = [
        path('',views.index),
        path('stusignup',views.stusignup),
        path('stusignin',views.stusignin),
        path('stusignup/stusignup',views.stusignup),
        path('stusignin/stusignin',views.stusignin),
        path('comsignup',views.comsignup),
        path('comsignin',views.comsignin),
        path('about',views.aboutus),  
]