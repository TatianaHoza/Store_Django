from django.core.management.base import BaseCommand
from django.utils import timezone
from store.storeapp.models import OrderModel
from store.storeapp.models import ClientModel
from store.storeapp.models import ProductModel
from random import choice


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        order = OrderModel(
            client=choice(ClientModel.objects.all()),
            total_price=0,
        )
        order.save()
        for _ in range(10):
            product = choice(ProductModel.objects.all())
            order.products.add(product)
            order.total_price += product.price

        print('Add new order')
