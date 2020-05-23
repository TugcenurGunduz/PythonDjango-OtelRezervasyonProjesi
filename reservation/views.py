from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from reservation.models import ReservationCart, ReservationCartForm
from product.models import Category


def index(request):
    return HttpResponse("Order App")


@login_required(login_url='/login')  # Check Login
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    checkroom = ReservationCart.objects.filter(room_id = id)  #Ürün sepette var mı sorgusu
    if checkroom:
        control = 1  # Ürün sepette var
    else:
        control = 0  # Ürün sepette yok

    if request.method == 'POST':  # form post edildiyse urun detay saufasinda
        form = ReservationCartForm(request.POST)
        if form.is_valid():
            if control==1:  # ürün varsa güncelle
                data = ReservationCart.objects.get(room_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # veritananina kaydet
            else :  #ürün yoksa ekle
                data = ReservationCart()  # model ile bağlantı kur
                data.user_id = current_user.id
                data.room_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
            request.session['cart_items'] = ReservationCart.objects.filter(user_id=current_user.id).count()
            messages.success(request, "Otel odasi basari ile eklenmistir. Teşekkür ederiz ")
            return HttpResponseRedirect(url)
    else:  # Ürün direk sepete ekle butonuna basıldıysa
        if control ==1:
            data = ReservationCart.objects.get(room_id=id)
            data.quantity += 1
            data.save()  # veritananina kaydet
        else:
            data = ReservationCart()   # model ile bağlantı kur
            data.user_id = current_user.id
            data.room_id = id
            data.quantity = 1
            data.save()     # veritabanina kaydet
            request.session['cart_items'] = ReservationCart.objects.filter(user_id=current_user.id).count()
        messages.success(request, "Otel odasi başarı ile sepete eklenmiştir. Teşekkür Ederiz ")
        return HttpResponseRedirect(url)

    messages.success(request, "Otel odasi sepete eklemede hata oluştu! Lütfen kontrol ediniz ")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')     # Check login
def reservationcart(request):
    category = Category.objects.all()
    current_user = request.user
    reservationcart = ReservationCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ReservationCart.objects.filter(user_id=current_user.id).count()
    total=0
    for rs in reservationcart:
        total += rs.room.price * rs.quantity

    context = {'reservationcart': reservationcart,
               'category': category,
               'total': total,
               }
    return render(request, 'reservationcart_rooms.html', context)


@login_required(login_url='/login')    # Check login
def deletefromcart(request, id):
    ReservationCart.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ReservationCart.objects.filter(user_id=current_user.id).count()
    messages.success(request, "Ürün sepetten Silinmiştir.")
    return HttpResponseRedirect("/reservationcart")