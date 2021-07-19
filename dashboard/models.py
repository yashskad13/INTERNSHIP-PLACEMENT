from django.db import models
from accounts.models import companyUser
# Create your models here.

class placementInfo(models.Model):
    company_name = models.ForeignKey(companyUser, default=None ,on_delete=models.CASCADE)
    package = models.CharField(default='', max_length=255)
    domain = models.CharField(max_length=255,default='')
    cgpa_req = models.FloatField(default=0)
    backlog = models.IntegerField(default=0)
    comimg = models.ImageField(upload_to='Images/')
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=13)
    company_website = models.URLField(default='')
    regform_link = models.URLField(default='')
    status = models.BooleanField(default=False)

class internshipInfo(models.Model):
    company_name = models.ForeignKey(companyUser, default=None ,on_delete=models.CASCADE)
    stipend = models.CharField(default='', max_length=255)
    domain = models.CharField(max_length=255,default='')
    cgpa_req = models.FloatField(default=0)
    workduration = models.IntegerField(default=0)
    modeofwork = models.CharField(default='', max_length=255)
    comimg = models.ImageField(upload_to='Images/')
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=13)
    company_website = models.URLField(default='')
    regform_link = models.URLField(default='')
    status = models.BooleanField(default=False)

