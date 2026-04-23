from django.urls import path
from .views import TourListView

urlpatterns = [
    path('list/', TourListView.as_view(), name='tour_list'),
]