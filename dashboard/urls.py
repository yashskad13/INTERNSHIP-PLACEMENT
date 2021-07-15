from django.urls import path
from . import views
urlpatterns = [
    path('',views.studashboard),
    path('comdashboard',views.comdashboard),
]