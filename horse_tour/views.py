from django.shortcuts import render
from .models import Location

def tour_list(request):
    locations = Location.objects.all()
    return render(request, 'tour_template.html', {'locations': locations})