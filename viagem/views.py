
from django.views.generic import ListView
from viagem.models import Viagem

class ListaViagens(ListView):
    model = Viagem
