from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Location


def tour_list(request):
    locations = Location.objects.all()

    paginator = Paginator(locations, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tour_template.html', {
        'page_obj': page_obj
    })