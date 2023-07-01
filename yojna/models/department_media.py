from django.db import models

from .base import BaseModel
from .department import DepartmentModel
import os
import uuid


def department_directory_path(instance, filename):
    path = os.path.join("departments", str(instance.department.pk))
    file_name = "{a}{b}".format(a=uuid.uuid4(), b=os.path.splitext(filename)[1])
    return os.path.join(path, file_name)


class DepartmentMediaModel(BaseModel):
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, default=None, null=True, blank=True,
                                   related_name='department_media')
    file_path = models.FileField(upload_to=department_directory_path, default=None, null=True, blank=True)

    class Meta:
        ordering = ['department__name']
        db_table = 'department_media'
        verbose_name = 'Department media'
        verbose_name_plural = 'Department media'
