from django.shortcuts import render, get_object_or_404
from .models import Client, Order, Product
from datetime import datetime, timedelta

def last_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    w_orders = Order.objects.filter(client=client,
                                    date_of_order__gte=datetime.now() - timedelta(days=10))
    m_orders = Order.objects.filter(client=client,
                                    date_of_order__gte=datetime.now() - timedelta(days=30))
    y_orders = Order.objects.filter(client=client,
                                    date_of_order__gte=datetime.now() - timedelta(days=365))
    context = {
        'client':client,
        'w_orders':w_orders,
        'm_orders':m_orders,
        'y_orders':y_orders,
    }
    return render(request, 'hw2/show_orders.html', context)

def order_info(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products = order.products.all()
    
    return render(request, 'hw2/products_info.html', {'order': order, 'products': products})