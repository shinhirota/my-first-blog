import pydicom

from django.shortcuts import render, redirect
from django.conf import settings
from .models import Dicom
from .forms import DicomForm

def upload(request):
    if request.method == 'POST':
        form = DicomForm(request.POST, request.FILES)
        if form.is_valid():
            saved_object = form.save()
            json = handle_uploaded_file(settings.MEDIA_ROOT + "/" + saved_object.file.name)

            return render(request, 'dicom/upload_result.html', {
                'form': form,
                'json': json,
            })
    else:
        form = DicomForm()
    return render(request, 'dicom/upload.html', {
        'form': form
    })

def handle_uploaded_file(filename):
    print(filename)
    dataset = pydicom.filereader.dcmread(filename)
    
    return dataset.to_json()
