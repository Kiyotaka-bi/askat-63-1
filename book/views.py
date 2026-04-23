from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()

        queryset = Book.objects.all()

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '').strip()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class FirstMessageView(View):
    def get(self, request):
        return HttpResponse("""
Лев Толстой: "Все счастливые семьи похожи друг на друга..."

Фёдор Достоевский: "Человек есть тайна..."

Александр Пушкин: "Чтение — вот лучшее учение."
""")