from django.shortcuts import render

def restaurants(request):
    return render(request, 'RESTAURANTS/restaurants.html')
