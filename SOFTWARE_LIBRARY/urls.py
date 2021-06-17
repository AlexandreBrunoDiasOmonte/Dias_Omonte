from django.urls.conf import path
from SOFTWARE_LIBRARY import views


app_name = 'SOFTWARE_LIBRARY'
urlpatterns = [
    path('', views.softwareLibrary, name='software-library'),
    path('details/<str:software_name>/', views.softwareDetails, name='details'),
    path('search/', views.search, name='search'),
    
]