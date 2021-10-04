from django.shortcuts import render, redirect
from .models import Dicom
from .forms import DicomForm

def upload(request):
    if request.method == 'POST':
        form = DicomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dicom/upload_result.html', {
                'form': form
            })
    else:
        form = DicomForm()
    return render(request, 'dicom/upload.html', {
        'form': form
    })
