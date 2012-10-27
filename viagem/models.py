from django.db import models

from ibge.models import Municipio


class Itinerario(models.Model):
    origem = models.ForeignKey(Municipio, related_name='origens')
    destino = models.ForeignKey(Municipio, related_name='destinos')
    duracao = models.TimeField()

class Empresa(models.Model):
    pass

class Viagem(models.Model):
    pass
