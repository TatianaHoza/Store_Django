from django.contrib import admin
from .models import ClientModel, OrderModel


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'adress']
    ordering = ['-name']
    list_filter = ['adress', 'phone']
    search_fields = ['phone']
    search_help_text = 'Поиск по полю Phone'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'products', 'date_ordered']
    ordering = ['-client']
    list_filter = ['date_ordered', 'total_price']
    search_fields = ['client']
    search_help_text = 'Поиск по полю Client'
    actions = [reset_quantity]

admin.site.register(ClientModel, ClientAdmin)
admin.site.register(OrderModel,OrderAdmin)
