from django.contrib import admin
from viagem.models import Itinerario, Viagem, Empresa


admin.site.register(Viagem)
admin.site.register(Empresa)
admin.site.register(Itinerario)
