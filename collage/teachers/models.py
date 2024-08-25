from django.db import models
from base.models import BaseModel
from departments.models import Departments
from collages.models import Collage
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class TeacherProfile(BaseModel):

    collage = models.ForeignKey(Collage, on_delete=models.CASCADE, null=True, blank=True, related_name='teacherCollage')
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacherProfile')
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, related_name='teacherDepartment', null=True, blank=True)
    teacher_image = models.ImageField(upload_to='teachers', null=True, blank=True)
    hiest_digree = models.CharField(max_length=100, null=True, blank=True)
    versity = models.CharField(max_length=100, null=True, blank=True)
    routine_img = models.ImageField(upload_to='routines', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def save(self, *args, **kwargs):
        teacher_full_name = f"{self.teacher.first_name} {self.teacher.last_name}" 
        self.slug = slugify(teacher_full_name)
        return super(TeacherProfile, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.teacher.first_name} {self.teacher.last_name}'