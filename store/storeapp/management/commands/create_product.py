from store.storeapp.models import ProductModel
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils import lorem_ipsum
import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for i in range(0, 10):
            products = ProductModel(name=f'product{i}', description=lorem_ipsum.paragraph(1),
                                    price=random.randint(100, 1000), quanty=random.randint(1, 20),
                                    date_added=timezone.now().date())
            products.save()
            print('Add new products')
