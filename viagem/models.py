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
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, null=True,
                                blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.nome


class Viagem(models.Model):

    TIPOS_DIA = (
        ('N', 'Normal'),
        ('F', 'Feriado'),
        ('D', 'Domingo'),
        ('S', 'Sábado'),
    )

    saida = models.TimeField()
    tipo_do_dia = models.CharField(max_length=1, choices=TIPOS_DIA,
                                   default='N')
    itinerario = models.ForeignKey(Itinerario)
    empresa = models.ForeignKey(Empresa)

    def __unicode__(self):
        tipo_do_dia = dict(self.TIPOS_DIA).get(self.tipo_do_dia)
        return u'{0} {1}: {2} - {3}'.format(tipo_do_dia,
                                            self.saida,
                                            self.itinerario,
                                            self.empresa)

    class Meta:
        verbose_name_plural = 'viagens'
