from django.db import models
from base.models import BaseModel #imported BaseModel

# Create your models here.


#Departmetns

class Departmets(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='departments', null=True, blank=True)

    def __str__(self) -> str:
        name = f'{self.name}'
        return name


