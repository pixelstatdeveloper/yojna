from django.db import models

from .base import BaseModel
from .sector import SectorModel


class DepartmentModel(BaseModel):
    sector = models.ForeignKey(SectorModel, on_delete=models.CASCADE, default=None, null=True, blank=True,
                               related_name='departments')
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.RESTRICT,
                               related_name='department_children')
    name = models.CharField(max_length=64, default=None, null=True, blank=True, db_index=True)
    description = models.TextField(default=None, null=True, blank=True)

    class Meta:
        ordering = ['name']
        db_table = 'department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    def __str__(self):
        return "{a}".format(a=self.name)
