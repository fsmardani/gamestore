from django.contrib import admin
from .models import Productbase,Category,ImageProduct
# Register your models here.
#admin.site.register(Productbase)
admin.site.register(Category)



class ImageInline(admin.StackedInline):
    model= ImageProduct
    extra=1

@admin.register(Productbase)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

