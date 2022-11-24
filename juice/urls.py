from django.contrib import admin
from django.urls import path,include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('main.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    re_path(r'auth/',include('djoser.urls.authtoken')),
    path('auth/',include('djoser.urls.authtoken')),
    path('api-auth',include('rest_framework.urls')),

]
