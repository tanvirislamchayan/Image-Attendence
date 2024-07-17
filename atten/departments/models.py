from django.db import models
from base.models import BaseModel #imported BaseModel

# Create your models here.


#Departmetns

class Departmets(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    short_name = models.CharField(max_length=30, null=True, blank=True)
    code = models.CharField(max_length=10,null=True, blank=True)
    image = models.ImageField(upload_to='departments', null=True, blank=True)

    def __str__(self) -> str:
        name = f'{self.code} - {self.name}'
        return name


