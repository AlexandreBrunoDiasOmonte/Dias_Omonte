from RESTAURANTS.models import CodePostal, Pays, Restaurant, Villes
from django.contrib import admin

@admin.register(CodePostal)
class CodePostalAdmin(admin.ModelAdmin):
    search_fields = ['codePostal_name']
    list_filter = ['codePostal_name']
    list_display = ['codePostal_name']
    ordering = ['codePostal_name']
    list_per_page = 10

@admin.register(Villes)
class VillesAdmin(admin.ModelAdmin):
    search_fields = ['ville_name', 'cp_name']
    list_filter = ['ville_name']
    list_display = ['ville_name', 'cp_name']
    ordering = ['ville_name']
    list_per_page = 10

@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    search_fields = ['pays_name']
    list_filter = ['pays_name']
    list_display = ['pays_name']
    ordering = ['pays_name']
    list_per_page = 10

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['restaurant_name', 'city', 'codePostal']
    list_filter = ['city']
    list_display = ['restaurant_name', 'adress', 'city', 'phone', 'webSite', 'image']
    ordering = ['restaurant_name']
    list_per_page = 10
