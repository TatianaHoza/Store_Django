
from django.urls import path
from .views import filter_client_orders, filter_ordered_products

urlpatterns = [
    path('client-orders/<int:client_id>', filter_client_orders, name='customer_orders'),
    path('ordered-products-by-period/<int:client_id>', filter_ordered_products,
         name='ordered_products_by_period'),
]