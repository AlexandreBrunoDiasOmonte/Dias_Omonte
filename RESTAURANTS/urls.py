from django.urls.conf import path
from RESTAURANTS import views


app_name = 'RESTAURANTS'
urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path('details/<str:resto_name>/', views.details, name='details'),
]
