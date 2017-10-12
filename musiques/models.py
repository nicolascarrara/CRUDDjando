# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Artiste(models.Model):
    nom = models.CharField(max_length=64)

    def __str__(self):
        return'{self.nom}'.format(self=self)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('musiques:artiste-detail', args=[str(self.id)])

class Morceau(models.Model):
    titre = models.CharField(max_length=64)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return'{self.titre}'.format(self=self).encode('utf-8')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('musiques:morceau-detail', args=[str(self.id)])
