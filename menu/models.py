from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['-time_create', 'name']


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название блюдо')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюды'
        ordering = ['-time_create', 'name']
