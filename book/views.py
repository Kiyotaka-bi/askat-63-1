from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404
from book.models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})





def first_message_view(request):
    if request.method == "GET":
        return HttpResponse("""
Лев Толстой: "Все счастливые семьи похожи друг на друга..."

Фёдор Достоевский: "Человек есть тайна..."

Александр Пушкин: "Чтение — вот лучшее учение."
""")
# Create your views here.



