# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError

from ibge.models import Municipio


class Itinerario(models.Model):
    origem = models.ForeignKey(Municipio, related_name='origens')
    destino = models.ForeignKey(Municipio, related_name='destinos')
    duracao = models.TimeField()

    def __unicode__(self):
        return u'{0} - {1}'.format(self.origem, self.destino)

    def save(self, *args, **kwargs):
        itinerario = Itinerario.objects.filter(
            origem=self.origem,
            destino=self.destino,
        )
        if not itinerario:
            super(Itinerario, self).save(*args, **kwargs)
        else:
            raise ValidationError('Itinerário já cadastrado')

class Empresa(models.Model):
    pass

class Viagem(models.Model):
    pass
