from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from product.models import Comment,CommentForm
from django.contrib.auth.decorators import login_required



def index(request):
    return HttpResponse("Product Page")


@login_required(login_url='/login') #Check Login
def addcomment(request,id):
    url = request.META.get('HTTP_REFERER') # get last url
    if request.method == 'POST': # form post edildiyse
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user # Access User Session information
            data = Comment() # model ile baglanti kur
            data.user_id = current_user.id
            data.product_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR') # Client computer ip address
            data.save() # veritabanina kaydet
            messages.success(request,"Yorumunuz basari ile gonderilmistir. Tesekkur Ederiz")
            return HttpResponseRedirect(url)

    messages.error(request,"Yorumunuz Kaydedilmedi. Lutfen Kontrol Ediniz")  
    return HttpResponseRedirect(url) 