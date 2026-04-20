from django.db import models

class Questionnaire(models.Model):
    
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    favorite_subject = models.CharField(max_length=50, verbose_name="Любимый предмет")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    likes_school = models.BooleanField(default=True, verbose_name="Любишь школу?")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата заполнения")
    email = models.EmailField(verbose_name="Электронная почта")
    bio = models.TextField(verbose_name="О себе")
    gpa = models.FloatField(verbose_name="Средний балл")
    avatar = models.ImageField(upload_to='avatars/', verbose_name="Твое фото")
    certificate = models.FileField(upload_to='certificates/', verbose_name="Твой документ")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return self.full_name

