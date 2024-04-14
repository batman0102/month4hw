from django.shortcuts import render, HttpResponse, get_object_or_404
import random
import datetime
from clothes.models import Clothes

def hello_view(request):
    if request.method == 'GET':
         return HttpResponse("Hello! It's my project")


def fun_view(request):
    if request.method == 'GET':
        jokes = [
            "Какой сыр любит сам себя? Фета!",
            "Что сказал 0 цифре 8? Привет, ремень!",
            "Почему программеры предпочитают темноту? Потому что в темноте нет багов!"
        ]
        joke = random.choice(jokes)
        return HttpResponse(joke)

def main_view(request):
    current_time = datetime.datetime.now()
    context = {
        'date': current_time.strftime("%d.%m.%Y"),
        'time': current_time.strftime("%H:%M:%S")
    }
    return render(request, 'main.html', context)

def clothes_list_view(request):
    if request.method == 'GET':
        clothes = Clothes.objects.all
        context = {'clothes': clothes}
        return render(request, 'clothes/clothes_list.html', context)

def clothes_detail_view(request, cloth_id=None):
    if request.method == 'GET':
        try:
            cloth = Clothes.objects.get(id=cloth_id)
        except Clothes.DoesNotExist:
            return HttpResponse('Cloth not found', status=404)

        context = {'cloth': cloth}

        return render(request, 'clothes/clothes_details.html', context)

