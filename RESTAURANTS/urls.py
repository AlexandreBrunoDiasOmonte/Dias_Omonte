from django.urls.conf import path
from RESTAURANTS import views


app_name = 'RESTAURANTS'
urlpatterns = [
    path('', views.restaurants, name='restaurants'),
]
