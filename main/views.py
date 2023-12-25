from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):


    context = {
        'title': 'OSPECHEV - Главная',
        'content': "Магазин мужской обуви OSPECHEV",
    }

    return render(request, 'main/index.html', context)


def about(request):

    return HttpResponse('Apout page')