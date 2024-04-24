from django.contrib import admin
from django.urls import path
from clothes.views import main_view, HelloView, ClothListView, ClothDetailView, CLothCreateView, ClothUpdateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", HelloView.as_view()),
    path('', main_view),
    path('clothes/', ClothListView.as_view(), name='clothes_list_view'),
    path('cloth/create/', CLothCreateView.as_view()),
    path('clothes/<int:cloth_id>/', ClothDetailView.as_view(), name='clothes_detail'),
    path("clothes/<int:cloth_id>/edit/", ClothUpdateView.as_view(), name='clothes_update_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

