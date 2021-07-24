from django.shortcuts import render
from accounts.models import studentUser,companyUser
# Create your views here.
suser = studentUser.objects.all()
cuser = companyUser.objects.all()

def studashboard(request):
    return render(request, 'studashboard.html',{'suser': suser,'cuser':cuser})

def stuprofile(request):
    return render(request, 'stuprofile.html',{'suser': suser,'cuser':cuser})

def stuplacement(request):
    return render(request, 'stuplacement.html',{'suser': suser,'cuser':cuser})

def stuinternship(request):
    return render(request, 'stuinternship.html',{'suser': suser,'cuser':cuser})

def stuall(request):
    return render(request, 'stuall.html',{'suser': suser,'cuser':cuser})



def comdashboard(request):
    return render(request, 'comdashboard.html',{'suser': suser,'cuser':cuser})

def comprofile(request):
    return render(request, 'comprofile.html',{'suser': suser,'cuser':cuser})

def complacement(request):
    return render(request, 'complacement.html',{'suser': suser,'cuser':cuser})

def cominternship(request):
    return render(request, 'cominternship.html',{'suser': suser,'cuser':cuser})

def comall(request):
    return render(request, 'comall.html',{'suser': suser,'cuser':cuser})
