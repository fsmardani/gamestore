from django.db import models

from django.contrib.postgres.fields import ArrayField

from GameStore.product.models import Productbase
from GameStore.Users.models import Normal_user, Vip_user


class ordering(models.Model):
    buyer_user = models.ForeignKey(Normal_user)
    product_ID = models.ForeignKey(Productbase.id, on_delete=models.RESTRICT)
    seller_user = models.ForeignKey(Vip_user)
    date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.buyer_user} <<- {self.product_ID} <<- {self.date} - {self.seller_user}"


class cart(models.Model):
    user_purch = models.ForeignKey(Normal_user)
    product_list = ArrayField(models.ForeignKey(ordering.id, on_delete=models.CASCADE))
    payment_status = models.BooleanField()
    #sum_of_score = sum(ArrayField(models.ForeignKey(to=product.rate)))
    date = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return f"{self.user_purch} - {self.date} -->> {self.product_list}"

