from django.contrib import admin
from django.urls import path
from clothes.views import hello_view, fun_view, main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('fun/', fun_view),
    path('main/', main_view)
]
