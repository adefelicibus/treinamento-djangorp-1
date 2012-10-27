# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Empresa'
        db.create_table('viagem_empresa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('viagem', ['Empresa'])

        # Adding model 'Viagem'
        db.create_table('viagem_viagem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('viagem', ['Viagem'])

        # Adding model 'Itinerario'
        db.create_table('viagem_itinerario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('origem', self.gf('django.db.models.fields.related.ForeignKey')(related_name='origens', to=orm['ibge.Municipio'])),
            ('destino', self.gf('django.db.models.fields.related.ForeignKey')(related_name='destinos', to=orm['ibge.Municipio'])),
            ('duracao', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('viagem', ['Itinerario'])


    def backwards(self, orm):
        # Deleting model 'Empresa'
        db.delete_table('viagem_empresa')

        # Deleting model 'Viagem'
        db.delete_table('viagem_viagem')

        # Deleting model 'Itinerario'
        db.delete_table('viagem_itinerario')


    models = {
        'ibge.municipio': {
            'Meta': {'ordering': "('nome', 'codigo_ibge')", 'object_name': 'Municipio'},
            'codigo_ibge': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'codigo_mesorregiao': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'codigo_microrregiao': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_capital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_polo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '8', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '8', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'populacao': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ibge.UnidadeFederativa']"})
        },
        'ibge.unidadefederativa': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'UnidadeFederativa'},
            'codigo_ibge': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'populacao': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'regiao': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'sigla': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        },
        'viagem.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'viagem.itinerario': {
            'Meta': {'object_name': 'Itinerario'},
            'destino': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destinos'", 'to': "orm['ibge.Municipio']"}),
            'duracao': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'origens'", 'to': "orm['ibge.Municipio']"})
        },
        'viagem.viagem': {
            'Meta': {'object_name': 'Viagem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['viagem']