from django.conf.urls import url
from .views import MorceauDetailView, MorceauUpdate, MorceauCreateView, MorceauListView, ArtisteCreateView, ArtisteUpdateView, ArtisteDetailView, ArtisteListView

app_name = 'musiques'  # Encapsule les urls de ce module dans le namespace musique
urlpatterns = [
    url(r'^$', MorceauListView.as_view(), name='morceau-liste'),
    url(r'^detail/(?P<pk>\d+)', MorceauDetailView.as_view(), name='morceau-detail'),
    url(r'^ajout/', MorceauCreateView.as_view(), name='morceau-ajout'),
    url(r'^liste/', MorceauListView.as_view(), name='morceau-liste'),
    url(r'^update/(?P<pk>\d+)', MorceauUpdate.as_view(), name='morceau-update'),
    url(r'^listeartiste/', ArtisteListView.as_view(), name='artiste-liste'),
    url(r'^detailartiste/(?P<pk>\d+)',
        ArtisteDetailView.as_view(), name='artiste-detail'),
    url(r'^ajoutartiste/', ArtisteCreateView.as_view(), name='artiste-ajout'),
    url(r'^updateartiste/(?P<pk>\d+)',
        ArtisteUpdateView.as_view(), name='artiste-update'),
]
