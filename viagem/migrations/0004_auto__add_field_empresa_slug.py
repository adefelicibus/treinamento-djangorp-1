# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Empresa.slug'
        db.add_column('viagem_empresa', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Empresa.slug'
        db.delete_column('viagem_empresa', 'slug')


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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
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
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['viagem.Empresa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itinerario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['viagem.Itinerario']"}),
            'saida': ('django.db.models.fields.TimeField', [], {}),
            'tipo_do_dia': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'})
        }
    }

    complete_apps = ['viagem']