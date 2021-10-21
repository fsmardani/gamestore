import re

from django.shortcuts import render
from product.models import Productbase,Category


def header(request):
    return render(request,'partials/header.html')


def footer(request):
    return render(request,'partials/footer.html')

def index(request):
    products = Productbase.objects.all().order_by('-added_time')[:4]
    categories=Category.objects.all()
    context = {'products': products,
               'cats': categories
               }
    return render (request,'index.html',context=context)

