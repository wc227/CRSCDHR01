from django.contrib import admin
from .models import *


# Register your models here.
class BasicInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'name', 'age', 'political_status', 'study_location', 'gender']


class WorkInfoAdmin(admin.ModelAdmin):
    list_display = ['company', 'post']


class EducationInfoAdmin(admin.ModelAdmin):
    list_display = ['school', 'education', 'degree', 'profession']


admin.site.register(BasicInfo, BasicInfoAdmin)
admin.site.register(WorkInfo, WorkInfoAdmin)
admin.site.register(EducationInfo, EducationInfoAdmin)
