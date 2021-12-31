from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import FileUploadModel

# Create your views here.

# open urls
def index(request):
    return render(request, 'index.html')

def str_smartfarm1(request):
    return render(request, 'str_smartfarm1.html')

def str_smartfarm2(request):
    return render(request, 'str_smartfarm2.html')

def kids_pattern1(request):
    return render(request, 'kids_pattern1.html')

def finedust1(request):
    return render(request, 'finedust1.html')


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
