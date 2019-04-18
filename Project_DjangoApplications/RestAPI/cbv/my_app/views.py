# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from my_app import models

class IndexView(TemplateView):
    template_name = 'index.html'

class HospitalListView(ListView):
    model = models.Hospital
    context_object_name = 'hospitals'

class HospitalDetailView(DetailView):
    context_object_name = 'hospital_detail'
    model = models.Hospital
    template_name = 'my_app/hospital_detail.html'

class HospitalCreateView(CreateView):
    fields = ('type', 'name', 'chiefphysician', 'location')
    model = models.Hospital

class HospitalUpdateView(UpdateView):
    fields = ('name', 'chiefphysician', 'type')
    model = models.Hospital

class HospitalDeleteView(DeleteView):
    model = models.Hospital
    success_url = reverse_lazy("my_app:list")
