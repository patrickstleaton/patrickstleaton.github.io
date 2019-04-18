# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Hospital(models.Model):
    type = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    chiefphysician = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("my_app:detail", kwargs={'pk':self.pk})


    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    hospital = models.ForeignKey(Hospital,related_name='patients')

    def __str__(self):
        return self.name
