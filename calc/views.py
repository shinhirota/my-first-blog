from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def home(request):
    return render(request, 'calc/home.html', {})
