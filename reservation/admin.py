from django.contrib import admin
from reservation.models import ReservationCart

class ReservationCartAdmin(admin.ModelAdmin):
    list_display = ['user','product','room','price','quantity','amount']
    list_filter = ['user']

admin.site.register(ReservationCart, ReservationCartAdmin)
