from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='изображение')
    description = models.TextField(verbose_name='описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='цена')

    def __str__(self):
        return self.title

class CartProduct(models.Model):

    user = models.ForeignKey('customer', verbose_name='покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('cart', verbose_name='корзина', on_delete=models. CASCADE)
    product = models.ForeignKey(Product, verbose_name='товар', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='общая цена')

    def __str__(self):
        return "продукт: {} (для корзины)".format(self.product.title)


