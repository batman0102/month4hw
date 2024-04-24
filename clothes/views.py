from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import datetime

from django.urls import reverse
from django.views.generic.edit import FormMixin

from clothes.models import Clothes
from clothes.forms import ReviewForm, ClothForm
from typing import Any
from django.forms.models import BaseModelForm
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')


def main_view(request):
    current_time = datetime.datetime.now()
    context = {
        'date': current_time.strftime("%d.%m.%Y"),
        'time': current_time.strftime("%H:%M:%S")
    }
    return render(request, 'main.html', context)


class ClothListView(ListView):
    model = Clothes
    template_name = 'clothes/clothes_list.html'
    context_object_name = 'clothes'

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        clothes = Clothes.objects.all()
        return clothes

class ClothDetailView(FormMixin, DetailView):
    model = Clothes
    template_name = 'clothes/clothes_details.html'
    context_object_name = 'cloth'
    pk_url_kwarg = 'cloth_id'
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('clothes_detail', kwargs={'cloth_id': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['reviews'] = self.object.reviews.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.clothes = self.object
        review.save()
        return super().form_valid(form)

class CLothCreateView(CreateView):
    model = Clothes
    form_class = ClothForm
    template_name = 'clothes/clothes_create.html'
    success_url = '/clothes/'

class ClothUpdateView(UpdateView):
    model = Clothes
    form_class = ClothForm
    template_name = 'clothes/clothes_edit.html'
    context_object_name = 'clothes'
    pk_url_kwarg = 'cloth_id'
    success_url = '/clothes/'


def cloth_update_view(request, cloth_id):
    try:
        post = Clothes.objects.get(id=cloth_id)
    except Clothes.DoesNotExist:
        return HttpResponse('Clooth not found', status=404)

    if request.method == 'GET':
        form = ClothForm(instance=post)

        context = {'form': form}

        return render(request, 'clothes/clothes_edit.html', context)

    elif request.method == 'POST':
        form = ClothForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()

            return redirect(f'/posts/{cloth_id}/')

        return render(request, 'clothes/clothes_edit.html', {'form': form})