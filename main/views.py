from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home'
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content_title': 'О нас',
        'content': 'Наш магазин существует уже более 10 лет и мы ни разу не оставляли наших клиентов не удовлетворенными',
    }

    return render(request, 'main/about.html', context)
