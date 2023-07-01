from django.db import models
from .scheme_registration_media import SchemeRegistrationMediaModel
from .base import BaseModel
from .department import DepartmentModel
from .sub_department import SubdepartmentModel
from .scheme import SchemeModel


class DocumentlinkModel(BaseModel):
    scheme = models.ForeignKey(SchemeModel, on_delete=models.CASCADE, default=None, null=True, blank=True,
                               related_name='scheme_documents')
    name = models.CharField(max_length=1000, null=True, blank=True, db_index=True)
    link = models.CharField(max_length=64, default=None, null=True, blank=True)
    class Meta:
        ordering = ['name']
        db_table = 'doc_table'
        verbose_name = 'doc_tables'
        verbose_name_plural = 'doc_tables'

    def __str__(self):
        return "{a}".format(a=self.name)
