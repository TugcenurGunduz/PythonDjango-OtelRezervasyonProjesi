from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from product.models import Product, Room


class ReservationCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.room.title

    @property
    def amount(self):
        if self.room_id is not None:
            return self.quantity * self.room.price

    @property
    def price(self):
        if self.room_id is not None:
            return self.room.price

class ReservationCartForm(ModelForm):
    class Meta:
        model = ReservationCart
        fields = ['quantity']