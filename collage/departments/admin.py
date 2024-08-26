from django.contrib import admin
from . models import Departments
from subjects.models import Subjects

# Register your models here.
class SubjectAdmin(admin.StackedInline):
    model = Subjects

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'collage']
    inlines = [SubjectAdmin]
admin.site.register(Departments, DepartmentAdmin)