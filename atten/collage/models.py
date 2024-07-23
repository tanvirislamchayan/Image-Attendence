from django.db import models
from base.models import BaseModel

# Create your models here.


class Collage(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=100)
    destrict = models.CharField(max_length=100)
    image = models.ImageField(upload_to='collage')
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
