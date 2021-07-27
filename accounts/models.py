from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class studentUser(models.Model):
    yourname = models.CharField(max_length=255, default='')
    branch = models.CharField(max_length=255, default='')
    yog = models.IntegerField(default=0)
    contact = models.CharField(max_length=13, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    email = models.EmailField()
    username = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.username


class companyUser(models.Model):
    companyname = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    contact = models.CharField(max_length=13, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    companyemail = models.EmailField()
    username = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')

    @staticmethod
    def comuser(ids):
        if ids:
            return companyUser.objects.filter(user=ids)
        else:
            return companyUser.objects.all()

    def __str__(self):
        return self.username
