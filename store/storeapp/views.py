from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from store.storeapp.models import ClientModel, OrderModel

def filter_client_orders(request, client_id):
    client = get_object_or_404(ClientModel, pk=client_id)
    orders = Order.objects.filter(client=client)
    context = {
        'client': client,
        'orders': orders,
    }
    return render(request, 'templates/orders.html', context)

def filter_ordered_products(request, client_id):
    client = get_object_or_404(ClientModel, pk=client_id)
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    orders_week = Order.objects.filter(client=client, order_date__gte=week_ago)
    orders_month = Order.objects.filter(client=clientr, order_date__gte=month_ago)
    orders_year = Order.objects.filter(client=client, order_date__gte=year_ago)

    products_week = set()
    products_month = set()
    products_year = set()

    for order in orders_week:
        products_week.update(order.products.all())

    for order in orders_month:
        products_month.update(order.products.all())

    for order in orders_year:
        products_year.update(order.products.all())

    context = {
        'client': client,
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year,
    }

    return render(request, 'templates/ordered_products_filter.html', context)




