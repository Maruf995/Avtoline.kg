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



class Shino(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Оборудование Шиномонтажа'
        verbose_name_plural = 'Оборудование Шиномонтажа'

class JacksCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории Домкратов'
        verbose_name_plural = 'Категории Домкратов'



class Jacks(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Домкраты'
        verbose_name_plural = 'Домкраты'


class CarLiftsCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории автомобильные подьемники'
        verbose_name_plural = 'Категории автомобильные подьемники'



class CarLifts(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Оборудование автомобильные подьемники'
        verbose_name_plural = 'Оборудование автомобильные подьемники'

class GarageCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории гаражные оборудование '
        verbose_name_plural = 'Категории гаражные оборудование '



class Garage(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'гаражные оборудование '
        verbose_name_plural = 'гаражные оборудование '

##############################################################################################

class ConsumablesCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории расходные материалы'
        verbose_name_plural = 'Категории расходные материалы'



class Consumables(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'расходные материалы'
        verbose_name_plural = 'расходные материалы'


class SparesCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории запчасти к оборудованию'
        verbose_name_plural = 'Категории запчасти к оборудованию'



class Spares(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'запчасти к оборудованию'
        verbose_name_plural = 'запчасти к оборудованию'

class BoxesCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории ящики с инструментами'
        verbose_name_plural = 'Категории ящики с инструментами'



class Boxes(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'ящики с инструментами'
        verbose_name_plural = 'ящики с инструментами'

class StandsCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории стенды'
        verbose_name_plural = 'Категории стенды'



class Stands(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'стенды'
        verbose_name_plural = 'стенды'

class GasolineCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории проверка бензонасосов'
        verbose_name_plural = 'Категории проверка бензонасосов'



class Gasoline(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Оборудование проверка бензонососов'
        verbose_name_plural = 'Оборудование проверка бензонососов'

class CamberToeCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=100)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории аппараты для развала схождение'
        verbose_name_plural = 'Категории аппараты для развала схождение'



class CamberToe(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
    image = models.ImageField(verbose_name='Фотографии', upload_to='Photo_Category')
    availiability = models.BooleanField(verbose_name="В Наличии",  null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Оборудование для развала схождение'
        verbose_name_plural = 'Оборудование для развала схождение'


