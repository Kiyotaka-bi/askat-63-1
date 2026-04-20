from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Book


def book_list(request):
    query = request.GET.get('q', '').strip()  # защита от None и пробелов

    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()  # чтобы не было дубликатов

    return render(request, 'book/book_list.html', {
        'books': books,
        'query': query
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})


def first_message_view(request):
    return HttpResponse("""
Лев Толстой: "Все счастливые семьи похожи друг на друга..."

Фёдор Достоевский: "Человек есть тайна..."

Александр Пушкин: "Чтение — вот лучшее учение."
""")