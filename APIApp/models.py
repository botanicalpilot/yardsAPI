from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class APIPlantRecord(models.Model):
    symbol = models.CharField(max_length=15, blank=True, default='')
    synonymSymbol = models.CharField(max_length=15, blank=True, default='')
    scientificNameAuthor = models.CharField(max_length=500, blank=True, default='' )
    nationalCommonName = models.CharField(max_length=500, blank=True, default='')
    family = models.CharField(max_length=250, blank=True, default='')
    nativeState = models.CharField(blank=False, max_length=100)


    class Meta:
        ordering = ['scientificNameAuthor']
    
    def __str__(self):
        return self.scientificNameAuthor + ":" + self.nationalCommonName