from django.urls import path,re_path
from .views import index, delete, edit, confirm


urlpatterns = [
    path('', index),
    re_path(r'^delete/(?P<oid>[0-9]+)$', delete),
    re_path(r'^edit/(?P<oid>[0-9]+)$', edit),
    re_path(r'^confirm/(?P<oid>[0-9]+)$', confirm)
]
