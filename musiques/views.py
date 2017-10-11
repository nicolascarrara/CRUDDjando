# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm 
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .models import Morceau
from django.utils import timezone
# Create your views here.


class MorceauListView(ListView):
    model = Morceau
    

class MorceauDetailView(DetailView):
    model = Morceau


class MorceauCreateView(CreateView):
    model = Morceau


class MorceauUpdate(UpdateView):
    model = Morceau
    template_name_suffix = '_update'


