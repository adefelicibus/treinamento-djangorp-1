
from django.conf.urls import patterns, include, url

urlpatterns = patterns('viagem.views',
    url(r'^$', 'lista_viagens', name='viagens'),
)
