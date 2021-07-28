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
    pObj = placementInfo.objects.all().order_by('company_name','-pk')
    return render(request, 'stuplacement.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj})


def stuinternship(request):
    iObj = internshipInfo.objects.all().order_by('company_name','-pk')
    return render(request, 'stuinternship.html', {'suser': suser, 'cuser': cuser, 'iObj': iObj})


def stuall(request):
    # ids = request.user.id
    # com_name = companyUser.objects.only('companyname').get(
    #     username=request.user.username).companyname
    # id = companyUser.objects.only('id').get(username=request.user.username).id
    pObj = placementInfo.objects.all().order_by('company_name','-pk')
    iObj = internshipInfo.objects.all().order_by('company_name','-pk')

    return render(request, 'stuall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj})


def comdashboard(request):
    return render(request, 'comdashboard.html', {'suser': suser, 'cuser': cuser})


def comprofile(request):
    return render(request, 'comprofile.html', {'suser': suser, 'cuser': cuser})


def complacement(request):
    ids = request.user.id
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    id = companyUser.objects.only('id').get(username=request.user.username).id
    pObj = placementInfo.placement_by_id(id)
    return render(request, 'complacement.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj})


def cominternship(request):
    ids = request.user.id
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    id = companyUser.objects.only('id').get(username=request.user.username).id
    iObj = internshipInfo.internship_by_id(id)
    return render(request, 'cominternship.html', {'suser': suser, 'cuser': cuser, 'iObj': iObj})


def comall(request):
    ids = request.user.id
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    id = companyUser.objects.only('id').get(username=request.user.username).id
    iObj = internshipInfo.internship_by_id(id)
    pObj = placementInfo.placement_by_id(id)
    return render(request, 'comall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj, 'com_name': com_name})
