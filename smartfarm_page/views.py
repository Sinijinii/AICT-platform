from django.shortcuts import render, redirect


# Create your views here.

# open urls
def index(request):
    return render(request, 'index.html')

def str_smartfarm1(request):
    return render(request, 'str_smartfarm1.html')

def kids_pattern1(request):
    return render(request, 'kids_pattern1.html')

def finedust1(request):
    return render(request, 'finedust1.html')


# file upload

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileUploadForm
from .models import FileUploadModel

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['uploadFromPC']
        uploadFile = FileUploadModel(
            file=file,
        )
        uploadFile.save()
        return redirect('fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'str_smartfarm1.html', context)