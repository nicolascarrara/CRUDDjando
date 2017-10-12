from django.conf.urls import url
from .views import MorceauDetailView, MorceauUpdate, MorceauCreateView, MorceauListView, ArtisteCreateView, ArtisteUpdateView, ArtisteDetailView, ArtisteListView

app_name = 'musiques'  # Encapsule les urls de ce module dans le namespace musique
urlpatterns = [
<<<<<<< HEAD
    url(r'^$',MorceauListView.as_view(),name='morceau-liste'), 
=======
    url(r'^$', MorceauListView.as_view(), name='morceau-liste'),
>>>>>>> d7c1951894b44fad728810c936fcd329ba379c2d
    url(r'^detail/(?P<pk>\d+)', MorceauDetailView.as_view(), name='morceau-detail'),
    url(r'^ajout/', MorceauCreateView.as_view(), name='morceau-ajout'),
    url(r'^liste/', MorceauListView.as_view(), name='morceau-liste'),
    url(r'^update/(?P<pk>\d+)', MorceauUpdate.as_view(), name='morceau-update'),
    url(r'^listeartiste/', ArtisteListView.as_view(), name='artiste-liste'),
<<<<<<< HEAD
    url(r'^detailartiste/(?P<pk>\d+)', ArtisteDetailView.as_view(), name='artiste-detail'),
    url(r'^ajoutartiste/', ArtisteCreateView.as_view(), name='artiste-ajout'),
    url(r'^updateartiste/(?P<pk>\d+)', ArtisteUpdateView.as_view(), name='artiste-update'),
=======
    url(r'^detailartiste/(?P<pk>\d+)',
        ArtisteDetailView.as_view(), name='artiste-detail'),
    url(r'^ajoutartiste/', ArtisteCreateView.as_view(), name='artiste-ajout'),
    url(r'^updateartiste/(?P<pk>\d+)',
        ArtisteUpdateView.as_view(), name='artiste-update'),
>>>>>>> d7c1951894b44fad728810c936fcd329ba379c2d
]
