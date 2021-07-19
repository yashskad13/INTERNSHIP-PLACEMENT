from django.contrib import admin
from .models import placementInfo,internshipInfo
# Register your models here.
class PlacementAdmin(admin.ModelAdmin):
    list_display=('company_name','package','domain','cgpa_req','backlog','comimg','company_email','company_phone','company_website','regform_link','status')
    
admin.site.register(placementInfo,PlacementAdmin)

class InternshipAdmin(admin.ModelAdmin):
    list_display=('company_name','stipend','domain','cgpa_req','workduration','modeofwork','comimg','company_email','company_phone','company_website','regform_link','status')
    
admin.site.register(internshipInfo,InternshipAdmin)
