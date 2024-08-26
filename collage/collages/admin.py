from django.contrib import admin
from .models import Collage
from teachers.models import TeacherProfile
from departments.models import Departments


# Register your models here.

class DepartmentAdmin(admin.StackedInline):
    model = Departments

class TeacherProfileAdmin(admin.StackedInline):
    model = TeacherProfile

class CollageAdmin(admin.ModelAdmin):
    inlines = [TeacherProfileAdmin, DepartmentAdmin]
    list_display = ['name', 'code']

admin.site.register(Collage, CollageAdmin)
