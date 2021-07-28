from django.shortcuts import render
from accounts.models import studentUser, companyUser
from dashboard.models import internshipInfo, placementInfo
# Create your views here.
suser = studentUser.objects.all()
cuser = companyUser.objects.all()

iinfo = internshipInfo.objects.all()
pinfo = placementInfo.objects.all()


def studashboard(request):
    return render(request, 'studashboard.html', {'suser': suser, 'cuser': cuser})


def stuprofile(request):
    return render(request, 'stuprofile.html', {'suser': suser, 'cuser': cuser})


def stuplacement(request):
    return render(request, 'stuplacement.html', {'suser': suser, 'cuser': cuser})


def stuinternship(request):
    return render(request, 'stuinternship.html', {'suser': suser, 'cuser': cuser})


def stuall(request):
    ids = request.user.id
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    id = companyUser.objects.only('id').get(username=request.user.username).id
    pObj = placementInfo.placement_by_id(id)
    iObj = internshipInfo.internship_by_id(id)
    return render(request, 'stuall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj, 'com_name': com_name})


def comdashboard(request):
    return render(request, 'comdashboard.html', {'suser': suser, 'cuser': cuser})


def comprofile(request):
    return render(request, 'comprofile.html', {'suser': suser, 'cuser': cuser})


def complacement(request):
    return render(request, 'complacement.html', {'suser': suser, 'cuser': cuser})


def cominternship(request):
    return render(request, 'cominternship.html', {'suser': suser, 'cuser': cuser})


def comall(request):
    ids = request.user.id
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    id = companyUser.objects.only('id').get(username=request.user.username).id
    pObj = placementInfo.placement_by_id(id)
    iObj = internshipInfo.internship_by_id(id)
    return render(request, 'comall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj, 'com_name': com_name})
