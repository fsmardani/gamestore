import os
from users.models import SupplierProfile
from django.db import models
# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=100)
    cat_parent = models.ForeignKey(to='Category',on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name


class Productbase(models.Model):
    devices=(
        ('ps4','ps4'),
        ('ps5','ps5'),
        ('all','all'),
        ('xbox','xbox'),
        ('nintendo', 'nintendo switch')
    )
    name = models.CharField(max_length=255)
    stock = models.BooleanField(default=False)
    device = models.CharField(max_length=20, choices=devices)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    price = models.FloatField(default=0.0)
    added_time = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(to=SupplierProfile ,on_delete=models.CASCADE)

    def __str__ (self):
        return self.name


class Cat_attr(models.Model):
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE)
    attr_name = models.CharField(max_length=255)

    def __str__(self):
        return self.attr_name


class Product_attr(models.Model):
    product = models.ForeignKey(to=Productbase,on_delete=models.CASCADE)
    cat_attr = models.ForeignKey(to=Cat_attr,on_delete=models.CASCADE)
    attr = models.CharField(max_length=255)

    def __str__(self):
        return self.attr


def model_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'{instance.__class__.__name__}/{instance.product.id}/{filename}'


class ImageProduct(models.Model):
    product = models.ForeignKey(Productbase, on_delete=models.CASCADE, related_name='img')
    image = models.ImageField(upload_to=model_image_directory_path)
    default = models.BooleanField(default=False)
