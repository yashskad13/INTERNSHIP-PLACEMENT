from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import studentUser
from django.contrib import auth

# Create your views here.


def index(request):
    return render(request, 'index.html')


def stusignup(request):
    print('kuchbhi')
    if request.method == 'POST':
        yourname = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['pass']
        password2 = request.POST['re_pass']
        email = request.POST['email']
        branch = request.POST['branch']
        yog = request.POST['yog']
        contact = request.POST['contact']
        print(yourname, username, password1, password2, email, yog, contact)

      #   if password1 == password2:
      #       if studentUser.objects.filter(username=username).exists():
      #          #  messages.info(request, 'Username is already Taken')
      #           print('1')
      #           return redirect('/stusignup')
      #       elif studentUser.objects.filter(email=email).exists():
      #           print('5')
      #          #  messages.info(request, 'Email is already Taken')
      #           return redirect('/stusignup')

        print('6')
        user = User.objects.create_user(
            username=username, password=password1)
        suser = studentUser(yourname=yourname,
                            email=email,yog=yog, contact=contact, branch=branch,user=user)
        auth.login(request,user)                    

        # user.is_active = False  # Example
        # send_email(user)
        #  return render(request, 'confirm_template.html', {'user': user})
        print(suser)
        suser.save()
        print('user created')
        return redirect('/stusignin')

          

    else:
        print('8')
        return render(request, 'stusignup.html')


def stusignin(request):
    return render(request, 'stusignin.html')


def comsignin(request):
    return render(request, 'comsignin.html')


def comsignup(request):
    return render(request, 'comsignup.html')


def aboutus(request):
    return render(request, 'aboutus.html')
