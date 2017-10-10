# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artiste(models.Model):
    nom=models.CharField(max_length=64)


class Morceau(models.Model):
    titre = models.CharField(max_length=64)
    artiste = models.ForeignKey(Artiste,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return'{self.titre} ({self.artiste})'.format(self=self)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('musiques.views.MorceauDetailView', args=[str(self.id)])
