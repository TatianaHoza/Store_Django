from django.core.management.base import BaseCommand
from store.storeapp.models import OrderModel



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = OrderModel.objects.filter(pk=pk).first()
        if order is not None:
            order.delete()
        self.stdout.write(f'Order: {order} deleted')