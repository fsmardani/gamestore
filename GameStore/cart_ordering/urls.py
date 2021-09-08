from django.urls import path
from .views import cart_list

urlpatterns = [
    path('cart-list/', cart_list.as_view(), name='cart-list'),
]
