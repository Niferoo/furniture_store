from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

# Create your views here.
def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content_title': 'О нас',
        'content': 'Наш магазин существует уже более 10 лет и мы ни разу не оставляли наших клиентов не удовлетворенными',
    }

    return render(request, 'main/about.html', context)
