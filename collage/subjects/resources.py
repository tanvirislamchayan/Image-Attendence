from import_export import resources
from . models import Subjects

class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subjects