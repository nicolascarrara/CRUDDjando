from django.conf.urls import url
from .views import MorceauDetailView, MorceauUpdate, MorceauCreateView

app_name = 'musiques'  # Encapsule les urls de ce module dans le namespace musique
urlpatterns = [
    url(r'^(?P<pk>\d+)/detail/', MorceauDetailView.as_view(), name='morceau-detail'),
    url(r'^ajout', MorceauCreateView.as_view(), name='morceau-ajout'),
    url(r'^(?P<pk>\d+)/update/', MorceauUpdate.as_view(), name='morceau-update'),
    url(r'^$',MorceauCreateView.as_view(), name='morceau-ajout'),
]
