from django.db import models

'''
id - Int
title - varchar
content - Text
created_at - DataTime 
update_at - DataTime 
photo - image
is_published - Boolean


Для чего класс типа Field
1. Какого типа будет создано поле в базе данных 
2. Какого типа будет создано поле в форме на стр. в браузере
3. Виляет на валидацию типа данных
'''


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')  # (blank=True) не обязательное поле для заполнения
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # сохраняет дату в публикации новости один раз при публикации
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')  # Дата изменяеться при обновленни(можно отслеживать изменения)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', verbose_name='Фото', blank=True)  # разбивает фотоки по дате.Требуеться устан. модуля"Pillow"
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):  # Стоковое представление
        return self.title  # Только по названию

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'  # verbose_name_plural Имя в множественном числе
        ordering = ['-created_at']  # Сортировка новостей


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория', db_index=True)  # db_index=True Индексирует поле, более быстрое для поиска.

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
