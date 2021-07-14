from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class studentUser(models.Model):
   yourname = models.CharField(max_length=255,default='')
   branch = models.CharField(max_length=255,default='')
   yog = models.IntegerField(default=0)
   contact = models.CharField(max_length=13,default='')
   user = models.OneToOneField(User, on_delete=models.CASCADE,default='')
   email = models.EmailField()