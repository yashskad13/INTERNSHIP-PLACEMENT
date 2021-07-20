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