from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")             
    description = models.TextField(verbose_name="Описание")                     
    publication_date = models.DateField(verbose_name="Дата публикации")                
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")  
    pages = models.IntegerField(verbose_name="Кол-во страниц")                         
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")      
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      
    cover = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name="Обложка")

    
    genres = models.ManyToManyField(Genre, related_name="books", verbose_name="Жанры")

    def __str__(self):
        return self.title


class BookCode(models.Model):
    code_number = models.CharField(max_length=50, unique=True, verbose_name="Инвентарный номер")
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="inventory_code")

    def __str__(self):
        return f"Код {self.code_number} для {self.book.title}"


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    author_name = models.CharField(max_length=100, verbose_name="Имя читателя")
    review_text = models.TextField(verbose_name="Текст отзыва")

    def __str__(self):
        return f"Отзыв от {self.author_name} на {self.book.title}"