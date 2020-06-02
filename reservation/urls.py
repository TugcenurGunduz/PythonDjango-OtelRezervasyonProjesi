from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('addtocart/<int:rid>/<int:pid>', views.addtocart, name='addtocart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('reservationroom/', views.reservationroom, name='reservationroom')

]