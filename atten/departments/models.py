from django.db import models
from base.models import BaseModel #imported BaseModel

# Create your models here.


#Departmetns

class Departmets(BaseModel):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='departments', null=True, blank=True)

    def __str__(self) -> str:
        name = f'{self.code} - {self.name}'
        return name


