from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):


    context = {
        'title': 'OSPECHEV - Главная',
        'content': "Магазин мужской обуви OSPECHEV",
        'name': "OSPECHEV",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'OSPECHEV - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }

    return render(request, 'main/about.html', context)