from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('upload/', permanent=False)),
    path('upload/', views.upload, name='upload'),
    path('ajax_upload/', views.ajax_upload, name='ajax_upload'),
]
