from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import studentUser,companyUser
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def stusignup(request):
    if request.method == 'POST':
        yourname = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['pass']
        password2 = request.POST['re_pass']
        email = request.POST['email']
        branch = request.POST['branch']
        yog = request.POST['yog']
        contact = request.POST['contact']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already Taken')
                return redirect('/stusignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already Taken')
                return redirect('/stusignup')
            else:
                user = User.objects.create_user(email=email,
                    username=username, password=password1)
                suser = studentUser(username=username, password=password1, yourname=yourname,
                            email=email, yog=yog, contact=contact, branch=branch, user=user)

                # user.is_active = False  # Example
                # send_email(user)
                #  return render(request, 'confirm_template.html', {'user': user})
                print(suser)
                suser.save()
                print('user created')
                return redirect('/stusignin')
        else:
            messages.info(request, 'Password is not matching')
            return redirect('/stusignup')

    else:
        return render(request, 'stusignup.html')


def stusignin(request):
    return render(request, 'stusignin.html')


def comsignin(request):
    return render(request, 'comsignin.html')


def comsignup(request):
    if request.method == 'POST':
        companyname = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['pass']
        password2 = request.POST['re_pass']
        companyemail = request.POST['email']
        address = request.POST['address']
        contact = request.POST['contact']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Company Username is already Taken')
                return redirect('/comsignup')
            elif User.objects.filter(email=companyemail).exists():
                messages.info(request, 'Email is already Taken')
                return redirect('/comsignup')
            else:
                user = User.objects.create_user(email=companyemail,
                    username=username, password=password1)
                cuser = companyUser(username=username, password=password1, companyname=companyname,
                            companyemail=companyemail, contact=contact, address=address, user=user)

                # user.is_active = False  # Example
                # send_email(user)
                #  return render(request, 'confirm_template.html', {'user': user})
                print(cuser)
                cuser.save()
                print('user created')
                return redirect('/comsignin')
        else:
            messages.info(request, 'Password is not matching')
            return redirect('/comsignup')

    else:
        return render(request, 'comsignup.html')



def aboutus(request):
    return render(request, 'aboutus.html')
