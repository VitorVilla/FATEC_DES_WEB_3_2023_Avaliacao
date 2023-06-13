from django.urls import path

from core import views

urlpatterns = [
    path('', views.post),
    path('listar/', views.get)
]
