from django.contrib import admin
from django.urls import path, include
from clothes.views import main_view, HelloView, ClothListView, ClothDetailView, CLothCreateView, ClothUpdateView, cloth_list_view
from django.conf.urls.static import static
from django.conf import settings

from user.views import RegisterView, LoginView, ProfileView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", HelloView.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', main_view, name='main_view'),
    # path('clothes/', ClothListView.as_view(), name='clothes_list_view'),
    path('clothes/', cloth_list_view, name='clothes_list_view'),
    path('cloth/create/', CLothCreateView.as_view()),
    path('clothes/<int:cloth_id>/', ClothDetailView.as_view(), name='clothes_detail'),
    path("clothes/<int:cloth_id>/edit/", ClothUpdateView.as_view(), name='clothes_update_view'),

    path("register/", RegisterView.as_view(), name = 'register_view'),
    path("login/", LoginView.as_view(), name = 'login_view'),
    path("profile/", ProfileView.as_view(), name = 'profile_view'),
    path("logout/", LogoutView.as_view(), name = 'logout_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

