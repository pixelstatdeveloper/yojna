from django.db import models

from .base import BaseModel


class SectorModel(BaseModel):
    name = models.CharField(max_length=64, default=None, null=True, blank=True, db_index=True)
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.RESTRICT,
                               related_name='sector_children')

    class Meta:
        ordering = ['name']
        db_table = 'sector'
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectors'

    def __str__(self):
        return "{a}".format(a=self.name)
