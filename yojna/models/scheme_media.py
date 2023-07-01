from django.db import models

from .base import BaseModel
from .scheme import SchemeModel
import os
import uuid


def scheme_directory_path(instance, filename):
    path = os.path.join("schemes", str(instance.scheme.pk))
    file_name = "{a}{b}".format(a=uuid.uuid4(), b=os.path.splitext(filename)[1])
    return os.path.join(path, file_name)


class SchemeMediaModel(BaseModel):
    INFORMATION = "information"
    REGISTRATION = "registration"

    CATEGORY_CHOICES = [
        (INFORMATION, "Information"),
        (REGISTRATION, "Registration"),
    ]
    scheme = models.ForeignKey(SchemeModel, on_delete=models.CASCADE, default=None, null=True, blank=True,
                               related_name='scheme_media')
    name = models.CharField(max_length=64, default=None, null=True, blank=True)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default=None, null=True, blank=True)
    file_path = models.FileField(upload_to=scheme_directory_path, default=None, null=True, blank=True)

    class Meta:
        ordering = ['scheme__name', 'name']
        db_table = 'scheme_media'
        verbose_name = 'Scheme media'
        verbose_name_plural = 'Scheme media'
