import logging

from django.http import Http404
from django.views.generic import ListView, DetailView
from viagem.models import Viagem, Empresa

class ListaViagens(ListView):
    model = Viagem

class EmpresaDetailById(DetailView):
    model = Empresa

    def get_queryset(self):
        logging.error("what the hell1")
        try:
            id_empresa = int(self.kwargs['pk'])
        except ValueError:
            raise Http404

        return Empresa.objects.filter(pk=id_empresa)
