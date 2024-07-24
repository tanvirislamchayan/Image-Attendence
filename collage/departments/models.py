from django.db import models
from base.models import BaseModel #imported BaseModel
from collages.models import Collage

# Create your models here.


#Departmetns

class Departments(BaseModel):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE, null=True, blank=True, related_name='department_of_collage')
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='departments', null=True, blank=True)

    def __str__(self) -> str:
        name = f'{self.name}'
        return name


