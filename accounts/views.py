from django.shortcuts import render

# Create your views here.

def index(request):
   return render(request,'index.html') 

def stusignup(request):
   return render(request,'stusignup.html')

def stusignin(request):
   return render(request,'stusignin.html')

def comsignin(request):
   return render(request,'comsignin.html')

def comsignup(request):
   return render(request,'comsignup.html')

def aboutus(request):
   return render(request,'aboutus.html')   