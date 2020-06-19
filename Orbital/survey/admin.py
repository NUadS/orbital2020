from django.contrib import admin
from .models import GenderFilter,SingaporeanFilter, FacultyFilter, YearFilter, ResidentialFilter,UploadSurvey,CompletedSurveys
# Register your models here.
admin.site.register(GenderFilter)
admin.site.register(SingaporeanFilter)
admin.site.register(FacultyFilter)
admin.site.register(YearFilter)
admin.site.register(ResidentialFilter)
admin.site.register(UploadSurvey)
admin.site.register(CompletedSurveys)
