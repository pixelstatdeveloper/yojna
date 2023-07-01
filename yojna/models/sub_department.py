from django.db import models
from .base import BaseModel
from .sector import SectorModel
from .department import DepartmentModel

class SubdepartmentModel(BaseModel):

    department = models.ForeignKey(DepartmentModel, default=None, null=True, blank=True, on_delete=models.RESTRICT,
                                   related_name='sub_department')

    name = models.CharField(max_length=1000, default=None, null=True, blank=True, db_index=True)

    class Meta:
        ordering = ['name']
        db_table = 'sub_department'
        verbose_name = 'Subdepartment'
        verbose_name_plural = 'Subdepartments'

    def __str__(self):
        return "{a}".format(a=self.name)


