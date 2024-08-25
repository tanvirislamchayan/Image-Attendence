from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Create your models here.


class Collage(BaseModel):
    # internal info
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        
        return super(Collage, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.code} - {self.name}'
