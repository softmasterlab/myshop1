from django.shortcuts import render
from .models import Order


def index(request):
    uid = request.user.id
    orders = Order.objects.filter(user_id=uid)
    data = dict()
    data['orders'] = orders
    return render(request, 'basket/index.html', context=data)


def delete(request, oid: int):
    pass


def edit(request, oid: int):
    pass


def confirm(request, oid: int):
    pass
