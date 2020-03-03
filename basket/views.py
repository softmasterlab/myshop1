from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm


def index(request):
    uid = request.user.id
    orders = Order.objects.filter(user_id=uid)
    data = dict()
    data['orders'] = orders
    return render(request, 'basket/index.html', context=data)


def delete(request, oid: int):
    data = dict()
    order = Order.objects.get(id=oid)
    if request.method == 'GET':
        data['order'] = order
        return render(request, 'basket/delete.html', context=data)
    elif request.method == 'POST':
        order.delete()
        return redirect('/basket')


def edit(request, oid: int):
    data = dict()
    order = Order.objects.get(id=oid)
    if request.method == 'GET':
        data['order'] = order
        data['form'] = OrderForm(instance=order)
        return render(request, 'basket/edit.html', context=data)
    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order.count = form.cleaned_data['count']
            order.save()
        return redirect('/basket')


def confirm(request, oid: int):
    pass
