from rest_framework import viewsets
from .models import CharacterStatistics, Ability
from .serializers import AbilitySerializer, CharacterStatisticsSerializer
from django.http import HttpResponse


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



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
