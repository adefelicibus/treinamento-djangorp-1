
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from viagem.views import ListaViagens
from viagem.models import Viagem


urlpatterns = patterns('viagem.views',
    url(r'^$', ListView.as_view(model=Viagem), name='viagens'),
    url(r'^privado$', login_required(ListaViagens.as_view()), name='viagens'),
)
