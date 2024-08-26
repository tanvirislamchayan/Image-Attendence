from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
admin.site.register(Semester)
admin.site.register(Probidhan)

@admin.register(Subjects)
class SubjectAdmin(ImportExportActionModelAdmin):
    list_display = ['name', 'code', 'department', 'semester', 'credits']