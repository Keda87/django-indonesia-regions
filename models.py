from __future__ import unicode_literals

from django.db import models
from django.db.models import PROTECT
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Province(models.Model):
    name = models.CharField(max_length=255)
    province_id = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Regency(models.Model):
    name = models.CharField(max_length=255)
    regency_id = models.CharField(max_length=80, unique=True)
    province = models.ForeignKey(Province, on_delete=PROTECT)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class District(models.Model):
    name = models.CharField(max_length=255)
    district_id = models.CharField(max_length=80, unique=True)
    regency = models.ForeignKey(Regency, on_delete=PROTECT)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Village(models.Model):
    name = models.CharField(max_length=255)
    village_id = models.CharField(max_length=80, unique=True)
    district = models.ForeignKey(District, on_delete=PROTECT)

    def __str__(self):
        return self.name
