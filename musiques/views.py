# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Morceau
# Create your views here.


class MorceauDetailView(DetailView):
    model = Morceau


class MorceauCreateView(CreateView):
    model = Morceau
    fields = ['artiste', 'titre']


class MorceauUpdate(UpdateView):
    model = Morceau
    fields = ['artiste', 'titre']
    template_name_suffix = '_update'
