#TO DO import


class CharacterStatistics(models.Model):
    '''
    To be changed
    '''
    name = models.CharField(max_length=255)
    damage = models.IntegerField()
    icon = models.CharField(max_length=255)
    rarity = models.CharField(max_length=20)
