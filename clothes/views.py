from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.db.models import Q
from .forms import SearchForm
from django.urls import reverse
from django.views.generic.edit import FormMixin

from clothes.models import Clothes
from clothes.forms import ReviewForm, ClothForm
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
    context_object_name = 'posts'
    paginate_by = 4
    def get_queryset(self):
        queryset = super().get_queryset().select_related('author').prefetch_related('tags')
        search = self.request.GET.get('search')
        tags = self.request.GET.getlist('tags')
        ordering = self.request.GET.get('ordering')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(text__icontains=search)
            )
        if tags:
            queryset = queryset.filter(tags__id__in=tags).distinct()
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET or None)

        total_posts = self.get_queryset().count()
        max_pages = total_posts // self.paginate_by
        if total_posts % self.paginate_by:
            max_pages += 1
        context['max_pages'] = range(1, max_pages + 1)

        return context


def cloth_list_view(request):
    if request.method == 'GET':
        clothes = Clothes.objects.all()

        search = request.GET.get('search')
        tags = request.GET.getlist('tags')
        ordering = request.GET.get('ordering')
        page = int(request.GET.get('page', 1))

        search_form = SearchForm(request.GET)
        clothes = Clothes.objects.all()

        if search:
            clothes = clothes.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
                )
        if tags:
            clothes = clothes.filter(tags__id__in=tags).distinct()

        if ordering:
            clothes = clothes.order_by(ordering)

        limit = 4
        max_pages = clothes.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page * limit

        clothes = clothes[start:end]

        context = {'clothes': clothes, 'search_form': search_form, 'max_pages': range(1, max_pages + 1)}

        return render(request, 'clothes/clothes_list.html', context)


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