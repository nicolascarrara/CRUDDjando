from django.conf.urls import url
from .views import accueil, MorceauDetailView, MorceauUpdate, MorceauCreateView, MorceauDeleteView, MorceauListView, ArtisteCreateView, ArtisteUpdateView, ArtisteDetailView, ArtisteListView, ArtisteDeleteView

app_name = 'musiques'  # Encapsule les urls de ce module dans le namespace musique
urlpatterns = [
    url(r'^$', accueil, name='accueil'),
    url(r'^detail/(?P<pk>\d+)', MorceauDetailView.as_view(), name='morceau-detail'),
    url(r'^ajout/', MorceauCreateView.as_view(), name='morceau-ajout'),
    url(r'^liste/', MorceauListView.as_view(), name='morceau-liste'),
    url(r'^update/(?P<pk>\d+)', MorceauUpdate.as_view(), name='morceau-update'),
    url(r'^delete/(?P<pk>\d+)', MorceauDeleteView.as_view(), name='morceau-delete'),
    url(r'^listeartiste/', ArtisteListView.as_view(), name='artiste-liste'),
    url(r'^detailartiste/(?P<pk>\d+)',
        ArtisteDetailView.as_view(), name='artiste-detail'),
    url(r'^ajoutartiste/', ArtisteCreateView.as_view(), name='artiste-ajout'),
    url(r'^updateartiste/(?P<pk>\d+)',
        ArtisteUpdateView.as_view(), name='artiste-update'),
    url(r'^deleteartiste/(?P<pk>\d+)',
        ArtisteDeleteView.as_view(), name='artiste-delete'),
]
