from django.db import models
from django.db.models import ImageField

'''Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа'''
#from .views import upload_image

class ClientModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=40)
    registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone:{self.phone}, adress: {self.adress}'


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quanty = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField(upload_to=upload_image)


class OrderModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

