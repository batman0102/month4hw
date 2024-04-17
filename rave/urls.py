from django.contrib import admin
from django.urls import path
from clothes.views import hello_view, fun_view, main_view, clothes_list_view, clothes_detail_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('fun/', fun_view),
    path('', main_view),
    path('clothes/', clothes_list_view),
    path('clothes/<int:cloth_id>/', clothes_detail_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)