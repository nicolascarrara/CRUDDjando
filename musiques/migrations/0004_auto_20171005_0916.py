# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 09:16
from __future__ import unicode_literals

from django.db import migrations

def migrer_artiste(apps, schema):
    Morceau = apps.get_model('musiques','Morceau')
    Artiste = apps.get_model('musiques','Artiste')
    for morcal in Morceau.objects.all():
        artiste_associe=Artiste.objects.get(nom=morcal.artiste)
        morcal.artiste_fk=artiste_associe
        morcal.save()

def annuler_migrer_artiste(apps, schema):
    Artiste = apps.get_model('musiques','Artiste')
    Artiste.objects.all().delete()
class Migration(migrations.Migration):

    dependencies = [
        ('musiques', '0003_auto_20171005_0902'),
    ]

    operations = [
    migrations.RunPython(migrer_artiste, reverse_code=annuler_migrer_artiste)
    ]
