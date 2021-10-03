from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Param
from .forms import ParamForm

def home(request):

    if request.method == "POST":
        form = ParamForm(request.POST)
        if form.is_valid():
            param = form.data
            result = _cal(int(param['arg1']), int(param['arg2']));
            return render(request, 'calc/result.html', {'param': param, 'result': result})

    form = ParamForm()
    return render(request, 'calc/home.html', {'form': form})


def _cal(a, b):
    return a + b;
