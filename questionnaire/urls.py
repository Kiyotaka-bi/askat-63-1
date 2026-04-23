from django.urls import path
from .views import (
    QuestionnaireListView,
    QuestionnaireCreateView,
    QuestionnaireUpdateView,
    QuestionnaireDeleteView,
    QuestionnaireDetailView
)

urlpatterns = [
    path('', QuestionnaireListView.as_view(), name='q_list'),
    path('create/', QuestionnaireCreateView.as_view(), name='q_create'),
    path('<int:pk>/update/', QuestionnaireUpdateView.as_view(), name='q_update'),
    path('<int:pk>/delete/', QuestionnaireDeleteView.as_view(), name='q_delete'),
    path('<int:pk>/', QuestionnaireDetailView.as_view(), name='q_detail'),
]