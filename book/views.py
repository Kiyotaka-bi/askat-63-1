from django.shortcuts import render
from django.http import HttpResponse

def first_message_view(request):
    if request.method == "GET":
        return HttpResponse("""
Лев Толстой: "Все счастливые семьи похожи друг на друга..."

Фёдор Достоевский: "Человек есть тайна..."

Александр Пушкин: "Чтение — вот лучшее учение."
""")
# Create your views here.
