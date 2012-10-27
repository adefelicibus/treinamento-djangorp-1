
from django.http import HttpResponse
from viagem.models import Viagem

def lista_viagens(request):

    buggy_str = ''
    for viagem in Viagem.objects.all():
        buggy_str += unicode(viagem) + '<br>'
    return HttpResponse(unicode(buggy_str))
