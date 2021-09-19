from django.contrib import admin
from .models import Productbase,Category,ImageProduct,Cat_attr,Product_attr
# Register your models here.
admin.site.register(Product_attr)
admin.site.register(Cat_attr)

class AttrInline(admin.StackedInline):
    model = Cat_attr
    extra = 3

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [AttrInline]


class ImageInline(admin.StackedInline):
    model = ImageProduct
    extra = 1

class AttrsInline(admin.StackedInline):
    model = Product_attr
    extra =1

@admin.register(Productbase)
class ProductAdmin(admin.ModelAdmin):
    inlines = [AttrsInline, ImageInline]

