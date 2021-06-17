from django.shortcuts import render

def home(request):
    return render(request, 'DIAS_OMONTE/home.html')