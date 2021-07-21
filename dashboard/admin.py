from django.contrib import admin
from .models import placementInfo, internshipInfo, Student_placement, Student_internship
# Register your models here.


class PlacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_username', 'package', 'domain', 'cgpa_req', 'backlog', 'comimg',
                    'company_email', 'company_phone', 'company_website', 'regform_link', 'status')


admin.site.register(placementInfo, PlacementAdmin)


class InternshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_username', 'stipend', 'domain', 'cgpa_req', 'workduration', 'modeofwork',
                    'comimg', 'company_email', 'company_phone', 'company_website', 'regform_link', 'status')


admin.site.register(internshipInfo, InternshipAdmin)


class StudentPlacementAdmin(admin.ModelAdmin):
    list_display = ('student_username', 'placement_id', 'status',)


admin.site.register(Student_placement, StudentPlacementAdmin)


class StudentInternshipAdmin(admin.ModelAdmin):
    list_display = ('student_username', 'internship_id', 'status',)


admin.site.register(Student_internship, StudentInternshipAdmin)
