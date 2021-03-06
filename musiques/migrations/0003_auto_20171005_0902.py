# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 09:02
from __future__ import unicode_literals

from django.db import migrations

def migrer_artiste(apps, schema):
# On récupère les modèles
    Morceau = apps.get_model('musiques','Morceau')
    Artiste = apps.get_model('musiques','Artiste')
# On récupère les artistes déjà enregsitrés dans la table Morceau
# Voir la documentation :
# - https://docs.djangoproject.com/fr/1.11/ref/models/querysets/#all
# - https://docs.djangoproject.com/fr/1.11/ref/models/querysets/#values
# - https://docs.djangoproject.com/fr/1.11/ref/models/querysets/#distinct
    artistes_connus = [fields['artiste']
        for fields in Morceau.objects.all().values('artiste').distinct()]
# On peuple la table Artiste
    for artiste in artistes_connus:
        Artiste.objects.create(nom=artiste)
def annuler_migrer_artiste(apps, schema):
    Artiste = apps.get_model('musiques','Artiste')
    Artiste.objects.all().delete()
class Migration(migrations.Migration):

    dependencies = [
        ('musiques', '0002_auto_20171005_0844'),
    ]

    operations = [
    migrations.RunPython(migrer_artiste, reverse_code=annuler_migrer_artiste)
    ]
