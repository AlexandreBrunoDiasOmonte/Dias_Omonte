from DIAS_OMONTE.settings import STATICFILES_DIRS
from django.db import models

class CodePostal(models.Model):
    codePostal_name = models.PositiveIntegerField('Code Postal', max_length=6, blank=False, primary_key=True)

    def __str__(self):
        return str(self.codePostal_name)

    class Meta:
        verbose_name = 'Code Postal'
        verbose_name_plural = 'Code Postaux'


class Villes(models.Model):
    ville_name = models.CharField('Ville', max_length=100, blank=False, primary_key=True)
    cp_name = models.ForeignKey(CodePostal, on_delete=models.PROTECT)

    def __str__(self):
        return self.ville_name

    class Meta:
        verbose_name = 'Ville'
        verbose_name_plural = 'Villes'


class Restaurant(models.Model):
    restaurant_name = models.CharField('Nom du restaurant', max_length=100, blank=False, primary_key=True)
    email = models.EmailField('Email', max_length=150, blank=True, editable=True)
    adress = models.CharField('Adresse du restaurant', max_length=200, blank=False)
    city = models.ForeignKey(Villes, on_delete=models.PROTECT)
    phone = models.CharField('Numéro de téléphone', unique=True, blank=True, max_length=20, editable=True)
    webSite = models.URLField('Site web', blank=True, editable=True)
    image = models.URLField('Lien de l\'image', blank=False)

    def __str__(self):
        return self.restaurant_name

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'