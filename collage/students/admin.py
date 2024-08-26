from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.

admin.site.register(GenDate)
admin.site.register(StudentShift)
admin.site.register(Attendence)

@admin.register(Student)
class StudentAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'roll', 'department', 'semester', 'collage')