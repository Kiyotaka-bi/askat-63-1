from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionnaire
from .forms import QuestionnaireForm


def q_list(request):
    anketas = Questionnaire.objects.all()
    return render(request, 'questionnaire/q_list.html', {'anketas': anketas})


def q_create(request):
    if request.method == "POST":
        form = QuestionnaireForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('q_list')
    else:
        form = QuestionnaireForm()
    return render(request, 'questionnaire/q_form.html', {'form': form, 'title': 'Создать анкету'})


def q_update(request, pk):
    anketa = get_object_or_404(Questionnaire, pk=pk)
    if request.method == "POST":
        form = QuestionnaireForm(request.POST, request.FILES, instance=anketa)
        if form.is_valid():
            form.save()
            return redirect('q_list')
    else:
        form = QuestionnaireForm(instance=anketa)
    return render(request, 'questionnaire/q_form.html', {'form': form, 'title': 'Изменить анкету'})


def q_delete(request, pk):
    anketa = get_object_or_404(Questionnaire, pk=pk)
    if request.method == "POST":
        anketa.delete()
        return redirect('q_list')
    return render(request, 'questionnaire/q_confirm_delete.html', {'anketa': anketa})


def q_detail(request, pk):
    anketa = get_object_or_404(Questionnaire, pk=pk)

    anketa.views += 1
    anketa.save()

    return render(request, 'questionnaire/q_detail.html', {
        'anketa': anketa
    })
