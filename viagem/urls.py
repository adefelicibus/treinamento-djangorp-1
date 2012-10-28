

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from viagem.views import ListaViagens
from viagem.models import Viagem, Empresa


urlpatterns = patterns('viagem.views',
    url(r'^$', ListView.as_view(model=Viagem), name='viagens'),
    url(r'^privado$', login_required(ListaViagens.as_view()),
        name='viagens'),
    url('^empresa/?$',
        ListView.as_view(model=Empresa), name='empresas'),
    url('^empresa/(?P<slug>[\w_-]+)/?$',
        DetailView.as_view(model=Empresa), name='empresa'),
)
