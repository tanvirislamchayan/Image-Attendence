from django.db import models
from base.models import BaseModel #imported BaseModel
from collages.models import Collage
from django.utils.text import slugify

# Create your models here.


#Departmetns

class Departments(BaseModel):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE, null=True, blank=True, related_name='department_of_collage')
    slug = models.SlugField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    field = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='departments', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Departments, self).save(*args, **kwargs)

    def __str__(self) -> str:
        name = f'{self.name}'
        return name


