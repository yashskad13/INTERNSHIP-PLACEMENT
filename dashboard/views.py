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
    return render(request, 'stuplacement.html', {'suser': suser, 'cuser': cuser, 'iinfo': iinfo, 'pinfo': pinfo})


def stuinternship(request):
    return render(request, 'stuinternship.html', {'suser': suser, 'cuser': cuser, 'iinfo': iinfo, 'pinfo': pinfo})


def stuall(request):
    return render(request, 'stuall.html', {'suser': suser, 'cuser': cuser, 'iinfo': iinfo, 'pinfo': pinfo})


def comdashboard(request):
    return render(request, 'comdashboard.html', {'suser': suser, 'cuser': cuser})


def comprofile(request):
    return render(request, 'comprofile.html', {'suser': suser, 'cuser': cuser})


def complacement(request):
    return render(request, 'complacement.html', {'suser': suser, 'cuser': cuser, 'iinfo': iinfo, 'pinfo': pinfo})


def cominternship(request):
    return render(request, 'cominternship.html', {'suser': suser, 'cuser': cuser, 'iinfo': iinfo, 'pinfo': pinfo})


def comall(request):
    ids = request.user.id
    print(ids)
    id = companyUser.objects.only('id').get(username=request.user.username).id
    print(id)
    pObj = placementInfo.placement_by_id(id)
    iObj = internshipInfo.internship_by_id(id)
    print(pObj)
    print(iObj)
    return render(request, 'comall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj})
