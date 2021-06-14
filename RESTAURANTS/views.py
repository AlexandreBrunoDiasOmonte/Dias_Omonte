from RESTAURANTS.models import Restaurant
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

def restaurants(request):
    restos = Restaurant.objects.order_by('restaurant_name')
    paginator = Paginator(restos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'RESTAURANTS/restaurants.html', context)

def details(request, resto_name):
    resto = get_object_or_404(Restaurant, pk=resto_name)
    context = {'resto': resto}
    return render(request, 'RESTAURANTS/details.html', context)
