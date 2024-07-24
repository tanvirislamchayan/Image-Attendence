from django.db import models
from base.models import BaseModel

# Create your models here.


class Collage(BaseModel):
    # internal info
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    establish_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    collage_image = models.ImageField(upload_to='collage_image')

    #location 
    area = models.CharField(max_length=100, null=True, blank=True)
    destrict = models.CharField(max_length=100)
    post_office = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)

    # details
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.code} - {self.name}'
