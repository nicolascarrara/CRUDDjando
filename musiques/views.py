# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from .models import Morceau, Artiste
from django.utils import timezone
# Create your views here.


class MorceauListView(ListView):
    model = Morceau


class MorceauDetailView(DetailView):
    model = Morceau


class MorceauCreateView(CreateView):
    model = Morceau
    fields = ['titre', 'artiste']


class MorceauDeleteView(DeleteView):
    model = Morceau

    def get_success_url(self):
        return reverse('musiques:morceau-liste')


class MorceauUpdate(UpdateView):
    model = Morceau
    fields = ['artiste', 'titre']
    template_name_suffix = '_update'


class ArtisteListView(ListView):
    model = Artiste


class ArtisteDetailView(DetailView):
    model = Artiste


class ArtisteCreateView(CreateView):
    model = Artiste
    fields = ['nom']


class ArtisteDeleteView(DeleteView):
    model = Artiste

    def get_success_url(self):
        return reverse('musiques:artiste-liste')


class ArtisteUpdateView(UpdateView):
    model = Artiste
    fields = ['nom']
    template_name_suffix = '_update'


def accueil(request):
    return render(request, 'musiques/accueil.html')
