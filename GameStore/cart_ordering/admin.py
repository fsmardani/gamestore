from django.contrib import admin

from GameStore.cart_ordering.models import ordering, cart

admin.site.regester(ordering)
admin.site.regester(cart)
