from django.db import models
from base.models import BaseModel
from departments.models import Departmets

# Create your models here.

class Semester(BaseModel):
    name = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Probidhan(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Subjects(BaseModel):
    department = models.ForeignKey(Departmets, null=True, blank=True, related_name='subjects_of_department', on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, null=True, blank=True, related_name='subjects_of_semester', on_delete=models.CASCADE)
    probidhan = models.ForeignKey(Probidhan, null=True, blank=True, related_name='subjects_of_probidhan', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=20, null=True, blank=True)
    theory = models.CharField(max_length=10, null=True, blank=True)
    practical = models.CharField(max_length=10, null=True, blank=True)
    credits = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.code}-{self.name}'

