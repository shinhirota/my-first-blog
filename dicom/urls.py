from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('upload/', permanent=False)),
    path('upload/', views.upload, name='upload'),
]
