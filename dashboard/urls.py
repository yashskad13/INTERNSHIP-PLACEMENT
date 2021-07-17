from django.urls import path
from . import views
from accounts.views import aboutus
urlpatterns = [
    path('',views.studashboard),
    path('comdashboard',views.comdashboard),
    path('about',aboutus),
]