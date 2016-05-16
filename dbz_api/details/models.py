from django.db import models


class CharacterStatistics(models.Model):
    name = models.CharField(max_length=255)
    birth_name = models.CharField(max_length=20)
    home_planet = models.CharField(max_length=255)
    power_level = models.IntegerField()
    highest_form = models.CharField(max_length=255)
    special_abilities = models.ForeignKey(
        'Ability',
        on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return "{}".format(self.name)

class Ability(models.Model):
    character = models.ManyToManyField(CharacterStatistics)
    ability_name = models.CharField(max_length=255)
    damage = models.IntegerField()
    ability_range = models.CharField(max_length=255)
    minimum_power_to_use = models.IntegerField()

# def details(render):
#     return render(request, '../templates/details/index.html', {'ability': ability})
