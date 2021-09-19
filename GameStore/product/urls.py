from django.contrib import admin
from django.urls import path
from .views import test,ProductList,ProductDetail




urlpatterns = [

    path('test',test),
    path('product-list/', ProductList.as_view(), name='product-list'),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name='product-detail')

]