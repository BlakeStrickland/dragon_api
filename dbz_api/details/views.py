from rest_framework import viewsets
from .models import CharacterStatistics, Ability
from .serializers import AbilitySerializer, CharacterStatisticsSerializer

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
