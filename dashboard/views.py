from django.shortcuts import render

# Create your views here.

def studashboard(request):
    return render(request, 'studashboard.html')

def comdashboard(request):
    return render(request, 'studashboard.html')