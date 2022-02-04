from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='изображение')
    description = models.TextField(verbose_name='описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='цена')

    def __str__(self):
        return self.title


#class NotebookProduct(Product):


class CartProduct(models.Model):

    user = models.ForeignKey('customer', verbose_name='покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('cart', verbose_name='корзина', on_delete=models.CASCADE, related_name='related_product')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='общая цена')

    def __str__(self):
        return "продукт: {} (для корзины)".format(self.product.title)


class Cart(models.Model):

    owner = models.ForeignKey('customer', verbose_name='владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='общая цена')

    def __str__(self):
        return str(self.id)

class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='номер телефона')
    address = models.CharField(max_length=255, verbose_name='адрес')

    def __str__(self):
        return "покупатель: {} {}".format(self.user.first_name,self.user.last_name)


class Notebooks(Product):

    diagonal = models.CharField(max_length=255, verbose_name='диагональ')
    display_type = models.CharField(max_length=255, verbose_name='тип дисплея')
    processor_freq = models.CharField(max_length=255, verbose_name='частота процессора')
    ram = models.CharField(max_length=255, verbose_name='оперативная память')
    video = models.CharField(max_length=255, verbose_name='видеокарта')
    time_without_charge = models.CharField(max_length=255, verbose_name='время работы аккумулятора')

    def __str__(self):
        return "{} {}".format(self.category.name, self.title)

class Smartphone(Product):
     diagonal = models.CharField(max_length=255, verbose_name='диагональ')
     display_type = models.CharField(max_length=255, verbose_name='тип дисплея')
     resolution = models.CharField(max_length=255, verbose_name='разрешение экрана')
     accum_volume = models.CharField(max_length=255, verbose_name='объем батареи')
     ram = models.CharField(max_length=255, verbose_name='оперативная память')
     sd = models.BooleanField(default=True)
     sd_volume_max = models.CharField(max_length=255, verbose_name='максимальный объем встраиваемой памяти')
     main_cam_mp = models.CharField(max_length=255, verbose_name='главная камера')
     frontal_cam_mp = models.CharField(max_length=255, verbose_name='фронтальная камера')

     def __str__(self):
         return "{} : {}".format(self.category.name, self.title)








