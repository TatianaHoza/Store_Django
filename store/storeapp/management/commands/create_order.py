from django.core.management.base import BaseCommand
from django.utils import timezone
from store.storeapp.models import OrderModel
from store.storeapp.models import ClientModel
from store.storeapp.models import ProductModel
from random import choice


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for i in range(0, 10):
            client = ClientModel.objects.all()
            products = ProductModel.objects.all()
            order = OrderModel(client=choice(client), products=choice(products),
                               total_price=sum(product.price for product in products),
                               data_ordered=timezone.now().date())
            order.save()
        print('Add new order')
