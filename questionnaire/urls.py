from django.urls import path
from . import views

urlpatterns = [
    path('', views.q_list, name='q_list'),
    path('create/', views.q_create, name='q_create'),
    path('<int:pk>/update/', views.q_update, name='q_update'),
    path('<int:pk>/delete/', views.q_delete, name='q_delete'),
    path('question/<int:pk>/', views.q_detail, name='q_detail'),
]