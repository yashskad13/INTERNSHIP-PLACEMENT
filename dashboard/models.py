from django.db import models
from accounts.models import companyUser, studentUser
# Create your models here.


class placementInfo(models.Model):
    company_username = models.ForeignKey(
        companyUser, default=None, on_delete=models.CASCADE)
    package = models.CharField(default='', max_length=255)
    domain = models.CharField(max_length=255, default='')
    cgpa_req = models.FloatField(default=0)
    backlog = models.IntegerField(default=0)
    comimg = models.ImageField(upload_to='Images/')
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=13)
    company_website = models.URLField(default='')
    regform_link = models.URLField(default='')
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class internshipInfo(models.Model):
    company_username = models.ForeignKey(
        companyUser, default=None, on_delete=models.CASCADE)
    stipend = models.CharField(default='', max_length=255)
    domain = models.CharField(max_length=255, default='')
    cgpa_req = models.FloatField(default=0)
    workduration = models.IntegerField(default=0)
    modeofwork = models.CharField(default='', max_length=255)
    comimg = models.ImageField(upload_to='Images/')
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=13)
    company_website = models.URLField(default='')
    regform_link = models.URLField(default='')
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Student_placement(models.Model):
    student_username = models.ForeignKey(
        studentUser, default=None, on_delete=models.CASCADE)
    placement_id = models.ForeignKey(
        placementInfo, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class Student_internship(models.Model):
    student_username = models.ForeignKey(
        studentUser, default=None, on_delete=models.CASCADE)
    internship_id = models.ForeignKey(
        internshipInfo, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
