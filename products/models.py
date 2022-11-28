from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(max_length=200, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name
