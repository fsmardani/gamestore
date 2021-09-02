from django.db import models
# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=100)
    cat_parent = models.ForeignKey(to='Category',on_delete=models.CASCADE,blank=True,null=True)


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

    def __str__ (self):
        return self.name


class ImageProduct(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Productbase, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/')
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name