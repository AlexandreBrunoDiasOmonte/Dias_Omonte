from RESTAURANTS.models import Restaurant
from django.contrib import admin

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['name', 'city', 'codePostal']
    list_filter = ['city']
    list_display = ['name', 'adress', 'city', 'phone', 'webSite', 'image']
    ordering = ['name']
    list_per_page = 10
