import re
from django.core.cache import cache
from django.shortcuts import render
from .models import Productbase,Category
from django.views.generic import ListView, DetailView
from django.db.models import Q


class ProductList(ListView):
    model = Productbase
    template_name = "productlist.html"
    context_object_name = "products"
    paginate_by = 20

    def get_queryset(self):
        product_qs = super().get_queryset()
        device_filter = self.request.GET.get('device', None)
        cat_filter = self.request.GET.get('cat', None)
        price_min_filter = self.request.GET.get('pmin', None)
        price_max_filter = self.request.GET.get('pmax', None)
        stock_filter = self.request.GET.get('stock', None)
        if stock_filter:
            if stock_filter=='نو':
                product_qs = product_qs.filter(stock=False)
            else:
                product_qs = product_qs.filter(stock=True)
        if device_filter:
            product_qs = product_qs.filter(device__contains=device_filter)
        if cat_filter:
            product_qs = product_qs.filter(category__name__contains=cat_filter)
        if price_min_filter:
            price_min_filter = re.sub("[نامحدود]", "0", price_min_filter)
            price_min_filter=float(re.sub("[a-z A-Z -%,. ]","",price_min_filter))

            pmin = Q(price__gte=price_min_filter)
        else:
            pmin = Q(price__gte=0)
        if price_max_filter:
            price_max_filter = re.sub("[نامحدود]", "100000000000000", price_max_filter)
            price_max_filter = float(re.sub("[a-z A-Z -%,. ]", "", price_max_filter))

            pmax = Q(price__lte=price_max_filter)
        else:
            pmax = Q(price__lte=100000000000000000)
        product_qs = product_qs.filter(pmin & pmax)
        return product_qs.order_by('added_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context


class ProductDetail(DetailView):
    model = Productbase
    template_name = "productdetail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        self.request.session["product_visit"] = self.request.session.get("product_visit", [])
        print(self.request.session["product_visit"])
        if self.kwargs['pk'] not in self.request.session["product_visit"]:
            self.request.session["product_visit"].append(self.kwargs['pk'])
            self.request.session.set_expiry(60*60*24)
            if not cache.get(f"product_visit_{self.kwargs['pk']}"):
                cache.set(f"product_visit_{self.kwargs['pk']}", 0)
            counter = cache.get(f"product_visit_{self.kwargs['pk']}") + 1
            print(counter)
            cache.set(f"product_visit_{self.kwargs['pk']}", counter)
        context = super().get_context_data(**kwargs)
        context['daily_view'] = cache.get(f"product_visit_{self.kwargs['pk']}")
        return context


def test(request):
    qs = Productbase.objects.all().order_by('added_time')[:6]
    context = {'products': qs}
    return render (request,'test.html',context=context)