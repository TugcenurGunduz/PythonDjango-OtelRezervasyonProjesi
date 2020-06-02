from django.contrib import admin
from reservation.models import ReservationCart, ReservationRoom, Reservation


class ReservationCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'room','date_start','date_end', 'price', 'quantity', 'amount']
    list_filter = ['user']


class ReservationRoomline(admin.TabularInline):
    model = ReservationRoom
    readonly_fields = ('user', 'room', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'total', 'status']
    list_filter = ['status']
    readonly_fields = (
        'user', 'address', 'city', 'country', 'phone', 'first_name', 'ip', 'last_name', 'phone', 'city', 'total')
    inlines = [ReservationRoomline]


class ReservationRoomAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'price', 'quantity', 'amount']
    list_filter = ['user']


admin.site.register(ReservationCart, ReservationCartAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationRoom, ReservationRoomAdmin)
