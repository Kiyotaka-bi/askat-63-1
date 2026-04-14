from django.contrib import admin
from book.models import Book
from .models import Genre, Book, BookCode, BookReview

# Регистрация основных моделей
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookCode)
admin.site.register(BookReview)

