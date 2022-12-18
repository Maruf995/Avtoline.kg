from django.db import models


# Create your models here.

class ShinoCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории Шиномонтажа'
        verbose_name_plural = 'Категории Шиномонтажа'

class BalansCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории Балансировочных Аппаратов'
        verbose_name_plural = 'Категорий Балансировочных Аппаратов'


class Shino(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Оборудование Шиномонтажа'
        verbose_name_plural = 'Оборудование Шиномонтажа'

class Balans(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии", null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Балансировочные Аппараты'
        verbose_name_plural = 'Балансировочные Аппараты'