import uuid

from django.db import models

from users.models import normalUserProfile, vipUserProfile
from product.models import Productbase, Category


class Cart(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, unique=True)
    payment_status = models.BooleanField(default=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    user_p = models.ForeignKey(normalUserProfile, on_delete=models.CASCADE, default='61e21fecd0c145afa2061301d81d05e9')

    class Meta:
        unique_together = ('id', 'user_p',)

    def __str__(self):
        return f"{self.id}"

class Ordering(models.Model):
    buyer_user = models.ForeignKey(normalUserProfile, on_delete=models.CASCADE)
    product_ID = models.ForeignKey(Productbase, on_delete=models.RESTRICT, default="")
    seller_user = models.ForeignKey(vipUserProfile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartinf', default="")

    def __str__(self):
        return f"{self.buyer_user}|{self.product_ID}|{self.date}|{self.seller_user}"
