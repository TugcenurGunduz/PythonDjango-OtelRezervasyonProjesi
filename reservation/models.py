from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from product.models import Product, Room


class ReservationCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    date_start = models.DateField()
    date_end = models.DateField()
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
        fields = ['quantity', 'date_start', 'date_end']


class Reservation(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    # date_start = models.DateField(blank=True)
    # date_end = models.DateField(blank=True)
    total = models.FloatField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name;


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'address', 'phone', 'city', 'country']


class ReservationRoom(models.Model):
    STATUS = {
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    }
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField()
    # date_start = models.DateTimeField()
    # date_end = models.DateTimeField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room.title
