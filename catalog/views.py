from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from basket.models import Order


def index(request):
    data = dict()
    goods = Product.objects.all()
    data['goods'] = goods
    return render(request, 'catalog/index.html', context=data)


def ajax_basket(request):
    response = dict()
    pid = request.GET['pid']
    uid = request.user.id
    sid = 1
    _count = 1
    Order.objects.create(count=_count, status_id=sid, product_id=pid, user_id=uid)
    response['mess'] = f'Заказ успешно сохранен для {request.user.username}'
    return JsonResponse(response)


def upload_basket(request):
    response = dict()
    uid = request.user.id
    orders = Order.objects.filter(user_id=uid)
    # Подсчет количества товаров
    count = 0
    for order in orders:
        count += order.count
    response['count'] = count
    # Подсчет общей стоимости товаров
    amount = 0
    for order in orders:
        amount += order.count * order.product.price
    response['amount'] = amount
    # Отправка данных:
    response['test'] = uid
    return JsonResponse(response)
