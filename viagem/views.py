
from django.shortcuts import render
from viagem.models import Viagem

def lista_viagens(request):

    return render(request, 'viagem/viagens.html', {
        'viagens': Viagem.objects.all()
    })
