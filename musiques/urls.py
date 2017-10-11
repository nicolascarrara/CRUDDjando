from django.conf.urls import url
from .views import MorceauDetailView, MorceauUpdate, MorceauCreateView, MorceauListView

app_name = 'musiques'  # Encapsule les urls de ce module dans le namespace musique
urlpatterns = [
    url(r'^detail/(?P<pk>\d+)', MorceauDetailView.as_view(), name='morceau-detail'),
    url(r'^ajout', MorceauCreateView.as_view(), name='morceau-ajout'),
    url(r'^liste', MorceauListView.as_view(), name='morceau-liste'),
    url(r'^update/(?P<pk>\d+)', MorceauUpdate.as_view(), name='morceau-update'),
    #url(r'^$',views.liste,name='liste'),
]
