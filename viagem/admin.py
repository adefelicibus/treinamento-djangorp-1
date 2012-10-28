# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from ibge.models import UnidadeFederativa

from viagem.models import Itinerario, Viagem, Empresa


class EmpresasOrigemUFFilter(SimpleListFilter):
    parameter_name = u'uf'
    title = u'Com origem no estado'

    def lookups(self, request, model_admin):
        return tuple((unicode(uf.codigo_ibge), uf.sigla)
                     for uf in UnidadeFederativa.objects.all())

    def queryset(self, request, queryset):
        if not self.value():
            return Empresa.objects.all()

        return Empresa.objects.filter(
            viagem__itinerario__origem__uf__codigo_ibge=self.value()
        ).distinct()


class ViagemInline(admin.TabularInline):
    model = Viagem


class EmpresaAdmin(admin.ModelAdmin):
    inlines = (ViagemInline, )
    prepopulated_fields = {"slug": ("nome",)}
    search_fields = ('nome', )
    list_filter = (EmpresasOrigemUFFilter, )


class ViagemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Viagem Base', {
            'fields': (
                'empresa',
                'itinerario',
                'saida',
            )
        }),
        ('Avançado', {
            'classes': ('collapse',),
            'fields': (
                'tipo_do_dia',
            ),
        })
    )


admin.site.register(Viagem, ViagemAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Itinerario)
