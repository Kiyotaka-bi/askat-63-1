from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionnaire
from .forms import QuestionnaireForm

# 1. Список всех анкет (Просмотр)
def q_list(request):
    anketas = Questionnaire.objects.all()
    return render(request, 'questionnaire/q_list.html', {'anketas': anketas})

# 2. Создание анкеты (Добавление)
def q_create(request):
    if request.method == "POST":
        form = QuestionnaireForm(request.POST, request.FILES) # FILES нужен для фото!
        if form.is_valid():
            form.save()
            return redirect('q_list')
    else:
        form = QuestionnaireForm()
    return render(request, 'questionnaire/q_form.html', {'form': form, 'title': 'Создать анкету'})

# 3. Редактирование (Изменение)
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

# 4. Удаление
def q_delete(request, pk):
    anketa = get_object_or_404(Questionnaire, pk=pk)
    if request.method == "POST":
        anketa.delete()
        return redirect('q_list')
    return render(request, 'questionnaire/q_confirm_delete.html', {'anketa': anketa})
# Create your views here.
