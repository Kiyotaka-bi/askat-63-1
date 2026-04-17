from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('phone', 'city', 'birth_date', 'bio', 'favorite_genre')}),
    )
    list_display = ['username', 'email', 'phone', 'city', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
