from rest_framework import serializers
from .models import Ability, CharacterStatistics


class CharacterStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharacterStatistics
        fields = ('name', 'birth_name', 'home_planet', 'power_level')

class AbilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ability
        fields = ('character', 'ability_name', 'damage', 'ability_range', 'minimum_power_to_use')
