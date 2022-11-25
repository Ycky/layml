from django.urls import path

from main import views
from main.views import *

urlpatterns = [
    path('juice/body/',views.body,name='body'),
    path('juice/create/',views.create,name='create'),
    path('news/creat/',views.creat,name='creat'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('shop/', views.shop, name='shop'),

    path('juice/',JuiceAPIList.as_view()),
    path('shop/',SjopAPIList.as_view()),
    # path('juice/<int:pk>', JuiceAPIUpdate.as_view()),
    # path('juicedelete/<int:pk>/', JuiceAPIDestroyView.as_view()),

    path('juice/<int:pk>', JuiceAPIListDetail.as_view(), name='juice-detail'),
    path('juice/<int:pk>/update', JuiceAPIUpdates.as_view(), name='juice-update'),
    path('juice/<int:pk>/juice-delete', JuiceAPIDelete.as_view(), name='juice-delete'),

    path('news/',NewsAPIList.as_view(),name='news-detail'),
    # path('news/<int:pk>/', NewsAPIUpdate.as_view(),name='news-update'),
    # path('news-delete/<int:pk>/', NewsAPIDestroy.as_view(),name='news-delete'),
    path('news/<int:pk>', views.NewsAPIDetail.as_view(), name="news-detail"),
    path('news/<int:pk>/update', views.NewsAPIUpdates.as_view(), name="news-update"),
    path('news/<int:pk>/delete', views.NewsAPIDelete.as_view(), name="news-delete"),
]


