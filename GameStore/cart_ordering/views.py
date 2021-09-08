from django.shortcuts import render

from django.views.generic import ListView, DetailView

import users.models
from cart_ordering.models import Cart, Ordering
from product.models import Productbase


class cart_list(ListView):
    model = Cart
    template_name = 'cartlist.html'
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_i = self.request.GET.get('id','2')
        context['cutt'] = Ordering.objects.all().filter(cart_id=cart_i)
        return context
