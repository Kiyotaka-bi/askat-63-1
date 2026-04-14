from django.db import models

# Категории туров (Многие ко многим)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.name

# Местность тура
class Location(models.Model):
    title = models.CharField(max_length=100, verbose_name="Местность")
    description = models.TextField(verbose_name="Описание")
    # СВЯЗЬ 3: Многие ко многим (у местности много категорий, у категории много местностей)
    categories = models.ManyToManyField(Category, verbose_name="Категории")

    def __str__(self):
        return self.title

# Человек (Один к одному)
class Tourist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя туриста")
    # СВЯЗЬ 1: Один к одному (1 человек = 1 местность по условию)
    chosen_location = models.OneToOneField(Location, on_delete=models.CASCADE, verbose_name="Выбранная местность")

    def __str__(self):
        return self.name

# Комментарии (Один ко многим)
class Comment(models.Model):
    # СВЯЗЬ 2: Один ко многим (у одной местности много комментов)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='comments', verbose_name="Местность")
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Коммент к {self.location.title}"
# Create your models here.
