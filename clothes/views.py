from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import random
import datetime
from clothes.models import Clothes
from clothes.forms import ReviewForm, ClothForm


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
        clothes = Clothes.objects.all()
        context = {'clothes': clothes}
        return render(request, 'clothes/clothes_list.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Clothes, Review
from .forms import ReviewForm

def clothes_detail_view(request, cloth_id):
    cloth = get_object_or_404(Clothes, id=cloth_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.clothes = cloth
            review.save()
            return redirect('clothes_detail', cloth_id=cloth.id)
    else:
        form = ReviewForm()
    reviews = cloth.reviews.all()
    context = {
        'cloth': cloth,
        'form': form,
        'reviews': reviews
    }
    return render(request, 'clothes/clothes_details.html', context)



def cloth_create_view(request):
    if request.method == 'GET':
        form = ClothForm()
        return render(request, 'clothes/cloth_create.html', {'form': form})
    elif request.method == 'POST':
        form = ClothForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clothes_list_view')

        return render(request, 'clothes/cloth_create.html', {'form': form})