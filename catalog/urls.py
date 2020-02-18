from django.urls import path
from .views import index, ajax_basket


urlpatterns = [
    path('', index),
    path('ajax_basket', ajax_basket)
]
