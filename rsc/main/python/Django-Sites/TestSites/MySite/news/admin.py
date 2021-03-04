from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'title', 'created_at', 'update_at', 'is_published', 'category')  # Название колонок(id, title...)в админке
    list_display_links = ('id', 'title')  # Создание интерактивной ссылки в списке "Новостей"
    search_fields = ('title', 'content')  # Cоздание строки поиска
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)  # Регистрация моделей и компонентов админки
admin.site.register(Category, CategoryAdmin)
