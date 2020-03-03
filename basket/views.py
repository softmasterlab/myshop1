from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


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
    data = dict()
    order = Order.objects.get(id=oid)
    user_name = request.user.username
    user_email = request.user.email
    admin_email = 'softmasterlab@gmail.com'
    am = order.count * order.product.price
    data['am'] = am
    if request.method == 'GET':
        data['order'] = order
        return render(request, 'basket/confirm.html', context=data)
    elif request.method == 'POST':
        # Отправка почтового уведомления на admin_email:
        email = admin_email
        context = 'Сообщение о подтверждении заказа\n'
        context += '--------------------------------\n'
        context += f'Пользователь - {user_name}\n'
        context += f'Товар - {order.product.name}\n'
        context += f'Цена - {order.product.price}\n'
        context += f'Количество - {order.count}\n'
        context += f'Стоимость - {am}\n'
        context += '--------------------------------\n'
        context += f'Обратная связь - {user_email}\n'
        context += '--------------------------------\n'
        send_mail('Подтверждение заказа', context, "itstep.projects@gmail.com",
                  [email], fail_silently=False)
        data['mess'] = 'Заказ успешно принят!\nОжидайте сообщение о сроках и условиях доставки'
        return render(request, 'basket/confirm_res.html', context=data)
