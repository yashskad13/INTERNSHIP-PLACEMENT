from django.contrib import admin

# Register your models here.
from .models import studentUser
class StudentAdmin(admin.ModelAdmin):
    list_display=('yourname','email','branch','yog','contact')
    
admin.site.register(studentUser,StudentAdmin)
