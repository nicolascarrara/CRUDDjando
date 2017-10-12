# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .models import Morceau, Artiste
from django.utils import timezone
# Create your views here.


class MorceauListView(ListView):
    model = Morceau


class MorceauDetailView(DetailView):
    model = Morceau


class MorceauCreateView(CreateView):
    model = Morceau
<<<<<<< HEAD
    fields = ['titre']
=======
    fields = ['artiste', 'titre']

>>>>>>> d7c1951894b44fad728810c936fcd329ba379c2d

class MorceauUpdate(UpdateView):
    model = Morceau
    fields = ['artiste', 'titre']
    template_name_suffix = '_update'


class ArtisteListView(ListView):
    model = Artiste

<<<<<<< HEAD
class ArtisteDetailView(DetailView):
    model = Artiste

=======

class ArtisteDetailView(DetailView):
    model = Artiste


>>>>>>> d7c1951894b44fad728810c936fcd329ba379c2d
class ArtisteCreateView(CreateView):
    model = Artiste
    fields = ['nom']


class ArtisteUpdateView(UpdateView):
    model = Artiste
    fields = ['nom']
