from django.contrib import admin
from .models import Productbase,Category,ImageProduct,ProductFeatures
# Register your models here.
#admin.site.register(Productbase)
admin.site.register(Category)



class FeatureInline(admin.StackedInline):
    model= ProductFeatures
    extra=3

class ImageInline(admin.StackedInline):
    model= ImageProduct
    extra=1

@admin.register(Productbase)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline,FeatureInline]

