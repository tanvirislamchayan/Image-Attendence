from django.db import models
import uuid

'''This model is a base model of abstruc type. It will be used everywhare as a base'''

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Make sure it's an abstract model

    class Meta:
        abstract = True