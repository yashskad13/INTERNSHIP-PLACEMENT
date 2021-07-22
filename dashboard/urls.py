from django.urls import path
from . import views
from accounts.views import aboutus
urlpatterns = [
    path('',views.studashboard),
    path('comdashboard',views.comdashboard),
    path('about',aboutus),
    path('comprofile',views.comprofile),
    path('complacement',views.complacement),
    path('cominternship',views.cominternship),
    path('comall',views.comall),
]