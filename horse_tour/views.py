from django.views.generic import ListView
from .models import Location


class TourListView(ListView):
    model = Location
    template_name = 'tour_template.html'
    context_object_name = 'page_obj'  
    paginate_by = 3