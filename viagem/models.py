from django.db import models

from ibge.models import Municipio


class Itinerario(models.Model):
    origem = models.ForeignKey(Municipio)
    destino = models.ForeignKey(Municipio)
    duracao = models.TimeField()

class Empresa(models.Model):
    pass

class Viagem(models.Model):
    pass
