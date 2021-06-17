from django.db import models

class Category(models.Model):
    category_name = models.CharField('Catégorie du Logiciel', max_length=30, blank=False, primary_key=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'


class License(models.Model):
    license_name = models.CharField('Licence', max_length=100, blank=False, primary_key=True)

    def __str__(self):
        return self.license_name

    class Meta:
        verbose_name = 'Licence'
        verbose_name_plural = 'Licences'


class Developer(models.Model):
    developer_name = models.CharField('Auteur du Logiciel', max_length=50, blank=False, primary_key=True)
    developer_web_site = models.URLField('Site web du créateur du Logiciel', max_length=200, blank=True)

    def __str__(self):
        return self.developer_name

    class Meta:
        verbose_name = 'Developpeur'
        verbose_name_plural = 'Developpeurs'


class Software(models.Model):
    software_name = models.CharField('Nom du Logiciel', max_length=100, blank=False, primary_key=True)
    software_logo = models.URLField('Logo du Logiciel', max_length=200, blank=False)
    software_description = models.TextField('Description', blank=True)
    software_image = models.URLField('Image du Logiciel', max_length=200, blank=False)
    software_version = models.CharField('Version du Logiciel', max_length=20, blank=True)
    software_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    software_license = models.ForeignKey(License, on_delete=models.PROTECT)
    software_developer = models.ForeignKey(Developer, on_delete=models.PROTECT)
    software_source = models.URLField('Source du Logiciel', max_length=200, blank=False)
    software_download_size = models.CharField('Taille du fichier téléchargé', max_length=15, blank=True)

    def __str__(self):
        return self.software_name
    
    class Meta:
        verbose_name = 'Logiciel'
        verbose_name_plural = 'Logiciels'
