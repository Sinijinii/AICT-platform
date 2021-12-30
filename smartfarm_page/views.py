from django.shortcuts import render

# Create your views here.

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




