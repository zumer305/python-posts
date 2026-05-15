from django.urls import path

from .views import create_post, update_post

urlpatterns = [
    path('create/', create_post),
        path('update/<int:pk>/', update_post),
]