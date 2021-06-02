from DIAS_OMONTE.settings import STATICFILES_DIRS
from django.db import models

class Restaurant(models.Model):
    name = models.CharField('Nom du restaurant', max_length=100, blank=False, primary_key=True)
    email = models.EmailField('Email', max_length=150, blank=True, editable=True)
    adress = models.CharField('Adresse du restaurant', max_length=200, blank=False)
    codePostal = models.BigIntegerField('Code Postal', default=75000, blank=False)
    city = models.CharField('Ville', max_length=200, default='Paris', blank=False)
    phoneIndicator = models.PositiveIntegerField('Indicateur du Pays', blank=True, editable=True)
    phone = models.CharField('Numéro de téléphone', unique=True, blank=True, max_length=15, editable=True)
    webSite = models.URLField('Site web', blank=True, editable=True)
    image = models.ImageField(upload_to=STATICFILES_DIRS[0] + 'MEDIAS/restaurants/')

    def __str__(self):
        return self.name