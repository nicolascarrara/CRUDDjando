from django.urls import reverse
from django.test import TestCase
from django.urls.exceptions import NoReverseMatch

from musiques.models import Morceau


class MorceauTestCase(TestCase):
    def setUp(self):
        Morceau.objects.create(titre='musique1')
        Morceau.objects.create(titre='musique2')
        Morceau.objects.create(titre='musique3')

    def test_morceau_url_name(self):
        try:
            url = reverse('musiques:morceau-detail', args=[1])
        except NoReverseMatch:
            assert False

    def test_morceau_url(self):
        morceau = Morceau.objects.get(pk=1)
        url = reverse('musiques:morceau-detail', args=[morceau.pk])
        response = self.client.get(url)
        assert response.status_code == 200
    
    def test_ajout_bd(self): 
        assert Morceau.objects.filter(pk=1).exists()


    def test_modif_bd(self):
        Morceau.objects.filter(pk=1).update(titre='test')
        morceau = Morceau.objects.get(pk=1)
        assert morceau.titre=='test'


    def test_delete_bd(self):
        assert Morceau.objects.filter(pk=1).delete()