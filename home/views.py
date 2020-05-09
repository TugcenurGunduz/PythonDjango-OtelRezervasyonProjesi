from unicodedata import category
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category, Images, Comment
from home.forms import SearchForm

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts= Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:10]
    randomproducts = Product.objects.all().order_by('?')[:4]

    context = {'setting': setting, 
                'category': category, 
                'page': 'home', 
                'sliderdata': sliderdata,
                'randomproducts':randomproducts,
                'lastproducts':lastproducts,
                'dayproducts':dayproducts
                }
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category,}   #{'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, }   #{'setting': setting, 'page': 'referanslar'}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):

    if request.method == 'POST': #form post ediliyor
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage() #model ile bağlantı kur
            data.name = form.cleaned_data['name'] #formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()#veritabanına kaydet
            data.save() #veritabanına kaydet
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür ederiz")
            return HttpResponseRedirect ('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    category = Category.objects.all()
    context = {'setting': setting, 'form': form, 'category': category, }   #{'setting': setting, 'page': 'iletisim'}
    return render(request, 'iletisim.html', context)


def category_products(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products': products,
                'category': category,
                'categorydata': categorydata}
    return render(request,'products.html',context)


def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id = id, status = 'True')
    context = { 'product':product,
                'category': category,
                'images':images,
                'comments': comments,
                }
    return render(request,'product_detail.html',context)


def product_search(request):
    if request.method == 'POST': # form post edildiyse
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query'] #formdan bilgiyi al
            products = Product.objects.filter(title__icontains=query) # Select * from product where title like fibue
            context = {
                'products': products,
                'category': category,
            }
            return render(request, 'products_search.html', context)
    return HttpResponseRedirect('/')