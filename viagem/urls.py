
from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from viagem.models import Viagem

urlpatterns = patterns('viagem.views',
    url(r'^$', ListView.as_view(model=Viagem), name='viagens'),
)
