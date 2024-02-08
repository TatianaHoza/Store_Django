import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from store.storeapp.models import ClientModel


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for i in range(0, 10):
            client = ClientModel(name=f'Client_{i}', email=f'client{i}@example.com',
                                 phone=random.randint(12345678, 87654321), adress=f'adress_{i}',
                                 registration=timezone.now().date())
            client.save()
        print('Add new client')
