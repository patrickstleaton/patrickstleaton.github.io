# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from my_app.models import Hospital, Patient
# Register your models here.

admin.site.register(Hospital)
admin.site.register(Patient)
