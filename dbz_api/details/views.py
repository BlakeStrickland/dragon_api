from rest_framework import viewsets
from .models import CharacterStatistics, Ability
from .serializers import AbilitySerializer, CharacterStatisticsSerializer
from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.template import loader



class CharacterStatisticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = CharacterStatistics.objects.all().order_by('name')
    serializer_class = CharacterStatisticsSerializer


class AbilitiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Ability.objects.all().order_by('ability_name')
    serializer_class = AbilitySerializer



def details(request):
    ability = Ability.objects.all().order_by('ability_name')

    template = loader.get_template('details/index.html')
    context = {
        'ability': ability,
    }
    return HttpResponse(template.render(context, request))


def create(request):
    pass 
