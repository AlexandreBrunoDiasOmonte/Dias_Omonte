from django.core.paginator import Paginator
from SOFTWARE_LIBRARY.models import Category, Software
from django.shortcuts import get_object_or_404, render

def softwareLibrary(request):
    softwares = Software.objects.all().order_by('software_name')
    categories = Category.objects.all()
    paginator = Paginator(softwares, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'software': softwares,
        'page_obj': page_obj,
        'categories': categories,
        'page_number':page_number
    }
    return render(request, 'SOFTWARE_LIBRARY/software-library.html', context)

def softwareDetails(request, software_name):
    software = get_object_or_404(Software, pk=software_name)
    software_description_char_count = len(software.software_description)
    print(software_description_char_count)
    logiciels = Software.objects.all().order_by('software_name')
    paginator = Paginator(logiciels, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'software_details': software,
        'page_number': page_number,
        'page_obj': page_obj,
        'software_description_char_count': software_description_char_count
    }
    return render(request, 'SOFTWARE_LIBRARY/software-details.html', context)

def search(request):
    categories = Category.objects.all().order_by('category_name')
    query = request.GET.get('query')
    if not query:
        software = Software.objects.all().order_by('software_name')
    else:
        # title contains the query is and query is not sensitive to case.
        software = Software.objects.filter(software_name__icontains=query).order_by('software_name')
    if not software.exists():
        software = Software.objects.filter(software_category__category_name__icontains=query).order_by('software_name')
    if not software.exists():
        software = Software.objects.filter(software_developer__developer_name__icontains=query).order_by('software_name')
    if not software.exists():
        software = Software.objects.filter(software_license__license_name__icontains=query).order_by('software_name')
    results = "Résultats pour la requête : %s" % query

    paginator = Paginator(software, 15)
    page_number = request.GET.get('page')
    page_obj_search = paginator.get_page(page_number)
    context = {
        'page_obj_search': page_obj_search,
        'results': results,
        'categories': categories,
        'page_number': page_number,
    }
    return render(request, 'SOFTWARE_LIBRARY/software-library-search.html', context)


def category(request, category_name):
    categories = Category.objects.all()
    all_software = Software.objects.all().order_by('software_name')
    software_categories = Software.objects.none()
    for software in all_software:
        if software.software_category.category_name == category_name:
            software_categories = Software.objects.filter(software_category__category_name=category_name)
    context = {
        'categories': categories,
        'software_categories': software_categories,
        'categoryName': category_name,
    }
    return render(request, 'SOFTWARE_LIBRARY/software-library-categories.html', context)