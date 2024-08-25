from django.db import models
from base.models import BaseModel
from subjects.models import Semester, Probidhan
from departments.models import Departments
from collages.models import Collage
from teachers.models import TeacherProfile
from subjects.models import Subjects

# Create your models here.

#model
class GenDate(BaseModel):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.teacher} - {self.date}'
    

class StudentShift(BaseModel):
    shift =  models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.shift
    


class Student(BaseModel):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE, null=True, blank=True, related_name='student_of_collage')
    name = models.CharField(max_length=100)
    sr_no = models.IntegerField()
    roll = models.IntegerField()
    registration = models.IntegerField()
    seasson = models.CharField(max_length=20)
    semester = models.ForeignKey(Semester, related_name='student_semester', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Departments, related_name='student_department', on_delete=models.SET_NULL, null=True, blank=True)
    probidhan = models.ForeignKey(Probidhan, related_name='student_probidhan', on_delete=models.SET_NULL, null=True, blank=True)
    shift = models.ForeignKey(StudentShift, related_name='student_shift', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

class Attendence(BaseModel):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE, null=True, blank=True, related_name='attendence_collage')
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=True, related_name='attendence_department')
    probidhan = models.ForeignKey(Probidhan, on_delete=models.SET_NULL, null=True, blank=True, related_name='attendence_probidhan')
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True, related_name='attendence_semester')
    group = models.ForeignKey(StudentShift, on_delete=models.SET_NULL, null=True, blank=True, related_name='attendence_group')
    date = models.DateField(null=True, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True, blank=True, related_name='attendence_subject')
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='attendence_teacher')

    present_students = models.ManyToManyField(Student, blank=True, related_name='present_attendences')
    absent_students = models.ManyToManyField(Student, blank=True, related_name='absent_attendences')
    
    def __str__(self) -> str:
        name = f"{self.department} - {self.date} - {self.collage}"
        return name

