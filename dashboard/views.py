from django.shortcuts import render
from accounts.models import studentUser,companyUser
# Create your views here.


def studashboard(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    return render(request, 'studashboard.html',{'suser': suser,'cuser':cuser})

def comdashboard(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    return render(request, 'comdashboard.html',{'suser': suser,'cuser':cuser})

def comprofile(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    return render(request, 'comprofile.html',{'suser': suser,'cuser':cuser})

def complacement(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    return render(request, 'complacement.html',{'suser': suser,'cuser':cuser})

def cominternship(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    return render(request, 'cominternship.html',{'suser': suser,'cuser':cuser})

def comall(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    return render(request, 'comall.html',{'suser': suser,'cuser':cuser})