from django.db import models
from base.models import BaseModel
from subjects.models import Semester, Probidhan
from departments.models import Departments
from collages.models import Collage

# Create your models here.

class GenDate(BaseModel):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.start_date} - {self.end_date}'
    

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