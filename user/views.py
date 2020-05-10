from django.http import HttpResponse
from django.shortcuts import render
from home.models import UserProfile
from product.models import Category


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile
               }
    return render(request, 'user_profile.html', context)
