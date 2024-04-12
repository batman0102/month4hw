from django.shortcuts import render, HttpResponse
import random
import datetime

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


