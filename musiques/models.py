# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Artiste(models.Model):
<<<<<<< HEAD
    nom=models.CharField(max_length=64)
    
    def __str__(self):
        return'{self.nom}'.format(self=self)
=======
    nom = models.CharField(max_length=64)

    def __str__(self):
        return'{self.nom}'.format(self=self).encode('utf-8')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('musiques:artiste-detail', args=[str(self.id)])
>>>>>>> d7c1951894b44fad728810c936fcd329ba379c2d

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('musiques:artiste-detail', args=[str(self.id)])

class Morceau(models.Model):
    titre = models.CharField(max_length=64)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True)

    def __str__(self):
<<<<<<< HEAD
        return'{self.titre}'.format(self=self)
=======
        return'{self.titre}'.format(self=self).encode('utf-8')
>>>>>>> d7c1951894b44fad728810c936fcd329ba379c2d

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('musiques:morceau-detail', args=[str(self.id)])
<<<<<<< HEAD
    
=======
>>>>>>> d7c1951894b44fad728810c936fcd329ba379c2d
