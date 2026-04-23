from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Questionnaire
from .forms import QuestionnaireForm


class QuestionnaireListView(ListView):
    model = Questionnaire
    template_name = 'questionnaire/q_list.html'
    context_object_name = 'anketas'


class QuestionnaireCreateView(CreateView):
    model = Questionnaire
    form_class = QuestionnaireForm
    template_name = 'questionnaire/q_form.html'
    success_url = reverse_lazy('q_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать анкету'
        return context


class QuestionnaireUpdateView(UpdateView):
    model = Questionnaire
    form_class = QuestionnaireForm
    template_name = 'questionnaire/q_form.html'
    success_url = reverse_lazy('q_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменить анкету'
        return context


class QuestionnaireDeleteView(DeleteView):
    model = Questionnaire
    template_name = 'questionnaire/q_confirm_delete.html'
    success_url = reverse_lazy('q_list')
    context_object_name = 'anketa'


class QuestionnaireDetailView(DetailView):
    model = Questionnaire
    template_name = 'questionnaire/q_detail.html'
    context_object_name = 'anketa'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj