from django.db import models
from base.models import BaseModel
from departments.models import Departmets
from django.contrib.auth.models import User

# Create your models here.

class TeacherProfile(BaseModel):

    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacherProfile')
    is_active = models.BooleanField(default=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(Departmets, on_delete=models.RESTRICT, related_name='teacherDepartment', null=True, blank=True)
    teacher_image = models.ImageField(upload_to='teachers', null=True, blank=True)
    hiest_digree = models.CharField(max_length=100, null=True, blank=True)
    versity = models.CharField(max_length=100, null=True, blank=True)
    routine_img = models.ImageField(upload_to='routines', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.teacher.first_name} {self.teacher.last_name}'