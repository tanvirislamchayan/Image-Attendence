from django.contrib import admin
from . models import TeacherProfile
from students.models import GenDate

# Register your models here.

class GenDateAdmin(admin.StackedInline):
    model = GenDate

class TeacherProfileAdmin(admin.ModelAdmin):
    inlines = [GenDateAdmin]
    list_display = ['teacher', 'collage']

admin.site.register(TeacherProfile, TeacherProfileAdmin)