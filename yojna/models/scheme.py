from django.db import models

from .base import BaseModel
from .department import DepartmentModel
from .sub_department import SubdepartmentModel


class SchemeModel(BaseModel):
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, default=None, null=True, blank=True,
                                   related_name='schemes')
    subdepartment = models.ForeignKey(SubdepartmentModel, on_delete=models.CASCADE, default=None, null=True, blank=True,
                                   related_name='scheme')
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.RESTRICT,
                               related_name='scheme_children')
    name = models.CharField(max_length=700, default=None, null=True, blank=True, db_index=True)
    description = models.TextField(default=None, null=True, blank=True)
    scheme_document_no = models.IntegerField(default=None, null=True, blank=True, db_index=True)

    # Newly added
    sample = models.FileField(upload_to='media', null=True, default=None,blank=True)
    url = models.URLField(null=True, default=None,blank=True)
    

    class Meta:
        ordering = ['name']
        db_table = 'scheme'
        verbose_name = 'Scheme'
        verbose_name_plural = 'Schemes'

    def __str__(self):
        return "{a}".format(a=self.name)
