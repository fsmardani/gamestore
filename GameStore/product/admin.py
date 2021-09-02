from django.contrib import admin

from GameStore.product.models import Category, Productbase, ImageProduct

admin.site.regester(Category)
admin.site.regester(Productbase)
admin.site.regester(ImageProduct)
